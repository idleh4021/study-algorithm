birds  = int(input())
num =0
answer=0
while birds > 0:
    num +=1
    if birds < num :
        num = 0
        continue
    else :
        birds -= num
        answer += 1
print(answer)

