import numpy as np

def solution(array):
    return [int(np.max(array)),array.index(int(np.max(array)))]