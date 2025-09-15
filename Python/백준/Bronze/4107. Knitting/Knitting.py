import sys

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    if arr[0]==arr[1]==arr[2]==0:break
    n,m,k = arr[0],arr[1],arr[2]
    patterns = list(map(int,sys.stdin.readline().split()))
    answer = n
    for i in range(0,m-1):
        n = patterns[ i % k]+n
        answer += n
    print(answer)
            
            
        
