arr = [],[]

def getQty(k, n):
    if arr[k][n-1] != -1:
        return arr[k][n-1]
    if k == 0:
        arr[k][n-1] = n
        return arr[k][n-1]
    if n == 1:
        arr[k][n-1] = 1
        return arr[k][n-1]
    else:
        arr[k][n-1] = getQty(k-1, n) + getQty(k, n-1)
        return arr[k][n-1]
    
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    arr =[[-1 for _ in range(n)] for _ in range(k+1)]
    print(getQty(k, n))