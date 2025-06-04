answer = 0
p = 0
for _ in range(4):
    a,b = map(int,input().split())
    p = p - a+b
    answer = p if p>answer else answer
print(answer)