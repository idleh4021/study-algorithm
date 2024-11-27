def solution(arr, queries):
    answer = []
    for query in queries:
        s,e,k = query
        arr = [val+1 if s<=idx and idx<=e and idx % k==0 else val for idx,val in enumerate(arr) ]
    return arr