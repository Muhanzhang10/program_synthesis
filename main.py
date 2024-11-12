import os 
from llm import LLM, Code
from generate_error_message import run_file
from loguru import logger
from dotenv import load_dotenv

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


def generate_iteration(question_title, model, iteration=3):
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
    

    for i in range(1, iteration):
        message, pass_rate = run_file(question_title, f"{output_file}_{str(i-1)}")

        logger.info(f"Pass rate is {pass_rate} for iteration {str(i-1)}")
        if pass_rate == 1:
            break
            
        prompt = iterative_prompt.replace("{REPORT}", message)
        prompt = prompt.replace("{QUESTION}", question)
        prompt = prompt.replace("{PYTHON_CODE}", code)
        code = llm.run(prompt, Code).code
        
        with open(f"{question_title}/script/{output_file}_{i}.py", "w") as f:
            f.write(code)
            
    message, pass_rate = run_file(question_title, f"{output_file}_{str(iteration-1)}")
    logger.info(f"Pass rate is {pass_rate} for iteration {str(iteration-1)}")

    with open(f"{question_title}/script/{output_file}_final.py", "w") as f:
        f.write(code)



if __name__ == "__main__":
    question = "textJustification"
    model_name = "llama3-8b-8192"

    # generate_baseline(question, model_name)
    generate_iteration(question, model_name)