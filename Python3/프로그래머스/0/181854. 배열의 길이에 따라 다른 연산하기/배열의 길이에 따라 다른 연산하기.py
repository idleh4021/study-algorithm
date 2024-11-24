def solution(arr, n):    
    return [(i+(n if idx %2==1 else 0)) if len(arr)%2==0 else (i+(n if idx %2==0 else 0)) for idx,i in enumerate(arr) ]
