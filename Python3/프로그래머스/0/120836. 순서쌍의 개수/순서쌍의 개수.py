def solution(n):
    return len([i for i in range(1,n) if n%i ==0]) +1