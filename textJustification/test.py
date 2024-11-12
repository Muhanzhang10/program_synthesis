import os 
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generator_test import groundTruth


def  test_one(datum, ans):
    return ans == groundTruth(*datum["input"])
    