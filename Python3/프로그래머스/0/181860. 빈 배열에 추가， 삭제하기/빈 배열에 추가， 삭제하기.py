def solution(arr, flags):
    answer =[]
    for idx, flag in enumerate(flags):
        if flag:
            for i in range(arr[idx]*2):
                answer.append(arr[idx])
        else:
            answer = answer[:-arr[idx]]
    return answer