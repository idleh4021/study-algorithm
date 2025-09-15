import sys

while True:
    n = sys.stdin.readline().strip()
    if n =='#': break
    arr = n.split()
    answer = []
    for i in arr : 
        answer.append(i[::-1])
    print(*answer)
        