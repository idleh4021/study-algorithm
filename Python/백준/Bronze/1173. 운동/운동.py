import sys
N, m, M, T, R =map(int, sys.stdin.readline().strip('\n').split())
X = m
answer = 0
work = 0 
while True:
    if m+T>M : 
        answer= -1 
        break
    if X+T<=M:
        X+=T
        answer+=1
        work+=1
        if work==N:
            break
    else:
        X-=R
        if X<m: X=m
        answer+=1
print(answer)
    

