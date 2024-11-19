def solution(a, b):
    
    for i in range(2,1001):
        while(a%i==0 and b%i==0):
            a=a//i
            b=b//i
    while(b%2==0 or b%5==0):
        b = b//2 if b%2==0 else b//5
    
    return 2 if(b!=1) else 1