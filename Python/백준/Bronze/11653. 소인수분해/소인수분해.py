answer  =[]
#in_nums = input()
max_nums = int(input())
cnt = max_nums
#in_nums,max_nums = int(in_nums),int(max_nums)
nums =[]

for i in range(2,cnt+1):
    if max_nums==1:
        break
    while max_nums%i==0:
        answer.append(i)
        max_nums/=i
        if max_nums==1:
            break
for i in answer:
    print(i)
