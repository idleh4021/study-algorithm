def solution(a, d, included):
    rag = list(range(a,len(included)*d+a,d))
    return sum([val for i,val in enumerate(rag) if included[i] ])