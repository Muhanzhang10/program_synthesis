import random
import json
import os 

def run():
    output = []
    lengths = [5, 7, 100, 1000, 10000]
    for length in lengths:
        for i in range(10):
            l = [random.randint(1, 100) for _ in range(length)]
            indices = random.sample(range(length), 2)
            s = l[indices[0]] + l[indices[1]]
            output.append({"input": [l, s], "output": indices})

    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
    with open(file_name, "w") as f:
        json.dump(output, f, indent=4) 
    
    
if __name__ == "__main__":
    run()