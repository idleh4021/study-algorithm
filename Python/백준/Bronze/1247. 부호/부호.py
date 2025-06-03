import sys
for _ in range(3):
    arr=0
    for i in range(int(sys.stdin.readline().strip())):
        arr+=int(sys.stdin.readline().strip())
    print('0' if arr==0 else '+' if arr>0 else '-')