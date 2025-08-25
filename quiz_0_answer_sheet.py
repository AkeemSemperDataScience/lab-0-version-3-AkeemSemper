import pandas as pd
import numpy as np

'''
This is a sample answer sheet for the autotested portion of the quiz.

For any parts where you are asked to write a function, please write your function
in the space provided below. Do not change the names or signatures of the functions if
they are specified in the question.

Your notebook file should use these functions, but they need to be independent of the notebook
and callable from anywhere. The assumption is that these files are general tools that could be used
in any project, and you are importing them into your notebook to use them in whatever analysis you are doing.
'''

def numberAdder(num_1, num_2):
    """
    Adds two numbers together.
    """
    return num_1 + num_2

def vowelsInString(string):
    """
    Counts the number of vowels in a given string.
    """
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in string if char in vowels)
    return count
