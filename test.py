import importlib
import os 
import json 
import sys 



question = "textJustification"
file_name = "llama3-8b-8192_iterative_0"

module = importlib.import_module(f"{question}.script.{file_name}")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{question}/data.json"), "r") as f: 
        data = json.load(f)

test_func = importlib.import_module(f"{question}.test").test_one

result = []
for i, datum in enumerate(data):
    ans = module.func(*datum["input"])
    result.append(test_func(datum, ans))
    
print(sum(result) / len(result))