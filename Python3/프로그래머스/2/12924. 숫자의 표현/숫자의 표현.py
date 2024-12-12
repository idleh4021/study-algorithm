def solution(n):
    answer = 0
    for i in range(n):
        num = i+1
        sum_v = 0
        while True:
            if n== sum_v:
                answer+=1
                break
            elif n<sum_v:
                break
            else :
                sum_v +=num
            num+=1
    return answer