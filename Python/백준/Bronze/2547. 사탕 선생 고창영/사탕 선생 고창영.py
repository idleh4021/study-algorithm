import sys
t = sys.stdin.readline().strip('\n')
answer =[]
p = 0
candy = 0
for _ in range(int(t)):
    i = sys.stdin.readline().strip('\n')
    if(i==''):
        p=candy=0
        p = int(sys.stdin.readline().strip('\n'))
        for j in range(p):
            candy+=int(sys.stdin.readline().strip('\n'))
        answer.append('YES' if candy%p==0 else 'NO')
    #else:
    #    candy+=i

[print(i) for i in answer]