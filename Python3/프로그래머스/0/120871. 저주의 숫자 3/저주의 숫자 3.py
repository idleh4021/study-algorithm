def solution(n):
    answer = 0
    list_number = [i for i in range(1,301) if ('3' not in str(i)  and not(i%3==0))]
    return list_number[n-1]