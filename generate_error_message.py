import os 
import json
import importlib


def generate_error_message(incorrect, error, pass_rate):
    incorrect = incorrect[:5]
    incorrect_cases = "\n".join([f"""Input: {str(datum['input'])}
                                 Correct answer: {str(datum['output'])}
                                 Your answer: {str(ans)}""" for ans, datum in incorrect])
    
    error = error[:5]
    error_cases = "\n".join([f"""Input: {str(datum["input"])}
                             Correct answer: {str(datum['output'])}
                             Your run time error message {err}""" for err, datum in error])
    
    prompt = f"""
        passing rate is {pass_rate} 
        """
        
    if incorrect_cases:
        prompt += f"""
        Error_cases:
        {incorrect_cases}
        """
    
    if error_cases:
        prompt += f"""
        Runtime_error_cases:
        {error_cases}
        """
    
    return prompt     
    
    

def run_file(question, file_name):
    module = importlib.import_module(f"{question}.script.{file_name}")
    test_func = importlib.import_module(f"{question}.test").test_one
    
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{question}/data.json"), "r") as f: 
        data = json.load(f)
    
    incorrect = []
    error = []
    for datum in data:
        try:
            ans = module.func(*datum["input"])
        except Exception as err:
            error.append((err, datum))
            continue   

        if not test_func(datum, ans):
            incorrect.append((ans, datum))
    pass_rate = 1 - (len(incorrect) + len(error)) / len(data)
    message = generate_error_message(incorrect, error, pass_rate)
    
    return message, pass_rate


if __name__ == "__main__":
    run_file("twoSum", "llama3-8b-8192_script_base.py")
        
            
             