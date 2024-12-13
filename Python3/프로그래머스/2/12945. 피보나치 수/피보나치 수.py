def solution(n):
    arr = [0,1]
    i = 2 
    while(i<=n):
        arr.append(arr[i-1]+arr[i-2])
        i+=1
    return arr[-1]%1234567
    
#    return fn(6)
'''
def fn(n):
    if n<1 : return 0
    elif n==1 : return 1
    return (fn(n-1)+fn(n-2))%1234567
'''