def solution(arr):
    answer = [i for i,val in enumerate(arr) if val==2]
    return arr[min(answer):max(answer)+1 ] if len(answer)>0 else [-1]