def solution(a, b):
    return a**2+b**2 if a%2==1 and b%2==1 else (a+b)*2 if a%2==1 or b%2==1 else abs(a-b)