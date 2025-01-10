answer  =0
cnt = input()
in_nums = input().split()

for i in in_nums:
    if int(i)==1:continue
    gs=[]
    for j in range(1,int(int(i)**0.5)+1):
        if int(i)%j ==0:
            gs.append(j)
    if len(gs)==1:
        answer+=1

print(answer)
