def solution(arr):
    return [i for idx,i in enumerate(arr) if idx==0 or(idx>0 and i!=arr[idx-1])]