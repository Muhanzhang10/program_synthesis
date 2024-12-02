import os 
from llm import LLM, Code
from generate_error_message import run_file
from loguru import logger
from dotenv import load_dotenv
import numpy as np 
import json 
import time 

load_dotenv(".secrets")


def generate_baseline(question_title, model):  
    output_file = model + "_baseline" 
    with open(os.path.join(question_title, "question.txt"), "r") as f:
        question = f.read()
    with open("baseline_prompt.txt", "r") as f:
        baseline_prompt = f.read()
        
    prompt = baseline_prompt.replace("{QUESTION}", question)
    llm = LLM(model)
    code = llm.run(prompt, Code).code
    
    with open(f"{question_title}/script/{output_file}.py", "w") as f:
        f.write(code)


def generate_iteration(question_title, model, iteration=10):
    output_file = model + "_iterative" 
    with open(os.path.join(question_title, "question.txt"), "r") as f:
        question = f.read()
    with open("baseline_prompt.txt", "r") as f:
        baseline_prompt = f.read()
    with open("iterative_prompt.txt", "r") as f:
        iterative_prompt = f.read()
    
    prompt = baseline_prompt.replace("{QUESTION}", question)
    llm = LLM(model)
    code = llm.run(prompt, Code).code
    
    with open(f"{question_title}/script/{output_file}_0.py", "w") as f:
        f.write(code)
    
    logs = np.zeros((5, iteration))
    for i in range(1, iteration):
        try:
            message, pass_rate, log = run_file(question_title, f"{output_file}_{str(i-1)}")
        except Exception as e:
            logger.error(f"Running error {e}")
            return logs.tolist()
            
        logs[:, i-1] = log
        
        logger.info(f"Pass rate is {pass_rate} for iteration {str(i-1)}")

            
        prompt = iterative_prompt.replace("{REPORT}", message)
        prompt = prompt.replace("{QUESTION}", question)
        prompt = prompt.replace("{PYTHON_CODE}", code)
        code = llm.run(prompt, Code).code
        
        with open(f"{question_title}/script/{output_file}_{i}.py", "w") as f:
            f.write(code)
            
        time.sleep(10)
            
    message, pass_rate, log = run_file(question_title, f"{output_file}_{str(iteration-1)}")
    logs[:, iteration-1] = log
    logger.info(f"Pass rate is {pass_rate} for iteration {str(iteration-1)}")

    with open(f"{question_title}/script/{output_file}_final.py", "w") as f:
        f.write(code)
        
    logs = logs.tolist()
    
    with open(f"{question_title}/experiment.json", "r") as f:
        d = json.load(f)
    
    d.append(logs)
    
    with open(f"{question_title}/experiment.json", "w") as f:
        json.dump(d, f, indent=4)



def generate_iteration_best_fit(question_title, model, iteration=10):
    output_file = model + "_iterative" 
    with open(os.path.join(question_title, "question.txt"), "r") as f:
        question = f.read()
    with open("baseline_prompt.txt", "r") as f:
        baseline_prompt = f.read()
    with open("iterative_prompt.txt", "r") as f:
        iterative_prompt = f.read()
    
    prompt = baseline_prompt.replace("{QUESTION}", question)
    llm = LLM(model)
    code = llm.run(prompt, Code).code
    
    with open(f"{question_title}/script/{output_file}_0.py", "w") as f:
        f.write(code)
    
    logs = np.zeros((5, iteration))
    message, pass_rate, log = run_file(question_title, f"{output_file}_0")
    logger.info(f"Pass rate is {pass_rate} for iteration 0")
    logs[:, 0] = log
    best = [message, code, pass_rate]
    
    
    for i in range(1, iteration):
    
        prompt = iterative_prompt.replace("{REPORT}", best[0])
        prompt = prompt.replace("{QUESTION}", question)
        prompt = prompt.replace("{PYTHON_CODE}", best[1])
        code = llm.run(prompt, Code).code
        
        with open(f"{question_title}/script/{output_file}_{i}.py", "w") as f:
            f.write(code)
            
        message, pass_rate, log = run_file(question_title, f"{output_file}_{str(i)}")
        logs[:, i] = log
        logger.info(f"Pass rate is {pass_rate} for iteration {str(i)}")
        
        if pass_rate > best[2]:
            best = [message, code, pass_rate]
        
        time.sleep(5)
            

    with open(f"{question_title}/script/{output_file}_final.py", "w") as f:
        f.write(best[1])
    
    
    logs = logs.tolist()
    
    with open(f"{question_title}/experiment2.json", "r") as f:
        d = json.load(f)
    
    d.append(logs)
    
    with open(f"{question_title}/experiment2.json", "w") as f:
        json.dump(d, f, indent=4)

    
        
#     return logs.tolist()


# def generate_iterations(question_title, model, iteration=10):
#     logs = []
#     for i in range(iteration):
#         log = generate_iteration(question_title, model, 10)
#         logs.append(log)
    
#     logger.success("Experiment done")
#     with open(f"{question_title}/logs.json", "w") as f:
#         json.dump(logs, f, indent=4)


if __name__ == "__main__":
    question = "textJustification"
    model_name = "llama3-8b-8192"

    # generate_baseline(question, model_name)
    # generate_iteration(question, model_name)
   

    generate_iteration_best_fit(question, model_name)