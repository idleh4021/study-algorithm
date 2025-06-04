import sys
while True:
    a = list(map(int,sys.stdin.readline().strip('\n').split()))
    answer = 1
    if len(a) == 1:
        break
    for idx,i in enumerate(a):
        if idx ==0: continue
        elif idx%2==1:
            answer *= i
        else:
            answer-=i
    print(answer)
