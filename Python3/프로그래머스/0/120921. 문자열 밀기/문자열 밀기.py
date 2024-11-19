def solution(A, B):
    cnt=0
    if(A==B):return 0
    for i in range(1,len(A)):
        a_val = A[-i:]+A[:-i]
        cnt+=1
        if(a_val==B): return cnt
    return -1
