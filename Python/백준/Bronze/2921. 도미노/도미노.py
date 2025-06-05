dots = int(input())
answer = 0
for i in range(0,dots+1):
    for j in range(i,dots+1):
        
        answer += i+j
print(answer)