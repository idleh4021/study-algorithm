def solution(arr, queries):
    answer = []
    for q in queries:
        s,e,k = q[0],q[1],q[2]
        try:
            result = min([val for val in arr[s:e+1] if(val>k)])
            answer.append(result)
        except:
            answer.append(-1)
    return answer