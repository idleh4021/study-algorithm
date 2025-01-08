n,idx = input().split()
n,idx = int(n),int(idx)
arr =[]
answer =0 
for i in range(1,n+1):
    if n%i ==0:
        arr.append(i)
    if len(arr)==idx:
        answer = i
        break
print(answer)
