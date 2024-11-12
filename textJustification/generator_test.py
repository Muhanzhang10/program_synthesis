import random
import json
import os 


def groundTruth(words, maxWidth):
        c = 0
        words.append(" "*maxWidth)
        ans = []
        line = []
        for i, w in enumerate(words):
            if c + len(line) - 1 + len(w) >= maxWidth:
                j = 0
                if len(line) == 1: line[0] += " "*(maxWidth-c)
                elif i == len(words) - 1:
                    for z in range(len(line)-1): line[z] += " "
                    line[-1] += " " * (maxWidth-len(line)+1 - c)
                else:
                    for _ in range(maxWidth - c):
                        if j < len(line) - 1: # if not the last word in line
                            line[j] += " "
                        j = (j+1)%(len(line)-1)
                ans.append("".join(line))
                c = 0
                line = []
            
            c += len(w)
            line.append(w)
        return ans


def run():
    output = []
    for level in range(5):
        if level == 0:
            maxWidth_num = 5
            word_length_num = 10
            word_num = 5
        elif level == 1:
            maxWidth_num = 20
            word_length_num = 50
            word_num = 5
        elif level == 2:
            maxWidth_num = 40
            word_length_num = 100
            word_num = 10
        elif level == 3:
            maxWidth_num = 60
            word_length_num = 200
            word_num = 15
        elif level == 4:
            maxWidth_num = 100
            word_length_num = 300
            word_num = 20
            
        
        for _ in range(10):
            maxWidth = random.randint(1, maxWidth_num)
            word_length = random.randint(1, word_length_num)
            words = []
            for i in range(word_length):
                words.append("x" * random.randint(1, word_num))
            
            ground_truth = groundTruth(words, maxWidth)
            output.append({"input": [words, maxWidth], "output": ground_truth})

    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
    with open(file_name, "w") as f:
        json.dump(output, f, indent=4) 
    
    
if __name__ == "__main__":
    run()