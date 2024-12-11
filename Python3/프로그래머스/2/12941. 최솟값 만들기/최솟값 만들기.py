def solution(A,B):
    a_sort = sorted(A)
    b_sort = sorted(B,reverse=True)
    answer = sum([ i*b_sort[idx] for idx,i in enumerate(a_sort)])
    return answer