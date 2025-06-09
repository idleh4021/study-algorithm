answer = 0

for i in range(8):
    #a= [i for idx,i in enumerate(input()) if (i%2 ==0 and idx%2==0 and i=='F') or (i%2 ==1 and idx%2==1 and i=='F')]
    answer +=len([c for idx,c in enumerate(input()) if (i%2 ==0 and idx%2==0 and c=='F') or (i%2 ==1 and idx%2==1 and c=='F')])
    
print(answer)