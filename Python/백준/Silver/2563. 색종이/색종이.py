white=[[0]*101 for i in range(101)]
answer=0
for i in range(int(input())):
    x,y = input().split()
    x,y = int(x),int(y)
    for j in range(y,y+10):
        for k in range(x,x+10):
            white[j][k] =1

for i in white:
    answer+= len([j for j in i if j==1])
print(answer)
    
    