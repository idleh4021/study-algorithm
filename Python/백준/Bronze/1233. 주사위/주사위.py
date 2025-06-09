import sys
a,b,c = map(int,sys.stdin.readline().strip('\n').split())
arr={}
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            if i+j+k in arr:
                arr[i+j+k]+=1
            else :
                arr[i+j+k]=1       
    
answer = max(arr,key=arr.get)
print(answer)
#print(arr)