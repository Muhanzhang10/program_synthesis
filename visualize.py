import json
import numpy as np 
import matplotlib.pyplot as plt

question = "textJustification"

with open(f"{question}/experiment.json", "r") as f:
    d = json.load(f)
    
d = np.array(d)[:-1]


def plot_all():

    fig, axes = plt.subplots(1, 5, figsize=(20, 6), sharey=True)
    fig.suptitle("TextJustification -mixtral-8x7b-32768 -Iterative optimization")

    for i, (data, ax) in enumerate(zip(range(5), axes)):
        
        one = d[:,i,:]
        for row in range(10):
            ax.plot(range(10), one[row], label=f'Row {row+1}')
        
        ax.set_xticks(range(10))
        ax.set_xlabel("Iteration")
        ax.set_title(f"Difficulty level {i+1}")
        if i == 0:
            ax.set_ylabel("Test case pass rate")
    plt.show()
    


def average():
    
    avg = d.mean(axis=0)
    for i in range(5):
        plt.plot(range(1, 11), avg[i], label=f'Difficulty level {i+1}') 
    
    plt.title("Average pass rate for all runs at every iteration")
    plt.ylabel("Average pass rate")
    plt.xlabel("Iteration")
    plt.xticks(range(10))
    plt.legend(loc="upper right")
    plt.show() 
    

average()