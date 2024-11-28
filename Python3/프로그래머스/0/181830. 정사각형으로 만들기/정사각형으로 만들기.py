def solution(arr):
    len_y = len(arr)
    len_x = len(arr[0])
    if len_y > len_x:
        for i in arr:
            i+=[0] *(len_y-len_x)
    elif len_x> len_y :
        for i in range(len_x-len_y):
            arr.append([0 for i in range(len_x)])
    return arr