def solution(array, n):
    array = sorted(array)
    idx = 0 
    if(n in array) : return n
    if(n< array[0]) : return array[0]
    if(n> array[-1]) : return array[-1]
    for index,val in enumerate(array):
        if(val<n) : continue
        numbers = [abs(array[index-1]-n),abs(val-n)]
        return array[index-1] if numbers[0]<=numbers[1] else val