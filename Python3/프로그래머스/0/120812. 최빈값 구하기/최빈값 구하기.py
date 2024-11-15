import numpy as np

def solution(array):
    num_list = set(array)
    cnt_list = []
    for i in list(num_list):
        cnt_list.append(array.count(i))
    
    answer=-1
    max_val = int(np.max(cnt_list))
    if cnt_list.count(max_val)>1 : return answer
    else : answer = list(num_list)[cnt_list.index(max_val)]
    
    return answer
