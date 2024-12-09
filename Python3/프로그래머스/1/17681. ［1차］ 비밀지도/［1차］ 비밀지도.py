def solution(n, arr1, arr2):
    answer = [i|arr2[idx] for idx,i in enumerate(arr1)]
    answer = [str(bin(i)).replace('0b','').zfill(n).replace('1','#').replace('0',' ') for i in answer]
    
    return answer