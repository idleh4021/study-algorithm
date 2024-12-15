def solution(arr):
    while(len(arr)>1):
        arr.append(lcm(arr.pop(),arr.pop()))
    '''
    if len(arr) == 1 : return arr[0]
    list_arr = []
    for i in range(len(arr)-1):#range(0,len(arr)-1,2):
        list_arr.append(lcm(arr[i],arr[i+1]))
    answer=0
    if len(list_arr) == 1: return list_arr[0]
    for i in range(len(list_arr)-1):
        for j in range(i+1,len(list_arr)):
            val = lcm(list_arr[i],list_arr[j])
        if answer<val : answer= val
    '''
    return arr[0]

def lcm(a,b):
    #result = 0
    result = a*b // gcd(a,b)
    return result

def gcd(a,b):
    #result = 0
    max_val  = max(a,b)
    min_val = min(a,b)
    
    while max_val % min_val != 0 :
        max_val,min_val =min_val, max_val % min_val
    result =  min_val
    
    return result