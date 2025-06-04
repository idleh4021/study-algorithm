import sys
cnt = int(sys.stdin.readline().strip('\n'))
answer=0
for i in range(cnt):
    answer+=int(sys.stdin.readline().strip('\n'))
    
print(answer-(cnt-1))
