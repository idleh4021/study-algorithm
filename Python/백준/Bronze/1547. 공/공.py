import sys
ball=1
cnt = int(sys.stdin.readline().strip('\n'))
for _ in range(cnt):
    a,b = map(int,sys.stdin.readline().strip('\n').split())
    if a ==ball or b==ball:
        ball = a if a!=ball else b
print(ball)

