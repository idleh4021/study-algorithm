def solution(n):
    answer = int(n/7 if n%7==0 else n/7+1)
    return answer