# test_two_sum.py
import os 
import sys 
import json 
import importlib


script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "script")
sys.path.append(script_path)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json"), "r") as f: 
    data = json.load(f)


def test_all():
    for script in os.listdir(script_path):
        if ".py" not in script:
            continue 
        module = importlib.import_module(script[:-3])
        for datum in data:
            ans = module.func(*datum["input"])
            l = datum["input"][0]
            assert l[ans[0]] + l[ans[1]] == datum["input"][1], "Answer is not correct"
    
    
def test_one(datum, ans):
    l = datum["input"][0]
    return l[ans[0]] + l[ans[1]] == datum["input"][1]
    





    
