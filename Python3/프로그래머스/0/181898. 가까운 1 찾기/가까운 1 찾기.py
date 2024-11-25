def solution(arr, idx):
    answer = [i for i,val in enumerate(arr) if idx<=i and val ==1]
    return answer[0] if len(answer)>0 else -1