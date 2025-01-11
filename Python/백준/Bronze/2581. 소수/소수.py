answer  =[]
in_nums = input()
max_nums = input()
in_nums,max_nums = int(in_nums),int(max_nums)


for num in range(in_nums,max_nums+1):
        if num==1:continue
        gs=[]
        for j in range(1,int(int(num)**0.5)+1):
            if int(num)%j ==0:
                gs.append(j)
                if len(gs)>1:
                    break
        if len(gs)==1:
            answer.append(num)
if len(answer)==0: print(-1)
else:
    print(sum(answer))
    print(answer[0])

