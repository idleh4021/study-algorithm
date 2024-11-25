def solution(arr):
    for i,val in enumerate(arr):
        for j,j_val in enumerate(val):
            if(arr[i][j]!= arr[j][i]):return 0
        
    return 1