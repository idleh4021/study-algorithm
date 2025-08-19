n = int(input())
arr = list(map(int,input().split()))
answer =[]
for idx,val in enumerate(arr):
    if len(answer)==0:
        answer.append(idx+1)
    else:
        if val ==0:
            answer.append(idx+1)
        else:
            answer.insert(abs(val-idx),idx+1)
print(*answer)        
