def solution(myString, pat):
    for i in range(len(myString)-1,-1,-1):
        if(myString[:i+1].endswith(pat)): return myString[:i+1]
        
    return answer
