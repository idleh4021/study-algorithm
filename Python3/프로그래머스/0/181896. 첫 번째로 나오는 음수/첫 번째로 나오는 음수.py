def solution(num_list):
    answer = [i for i in num_list if i<0]
    return -1 if len(answer)==0 else num_list.index(answer[0])