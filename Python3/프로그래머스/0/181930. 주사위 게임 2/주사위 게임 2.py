def solution(a, b, c):
    set_val = set([a,b,c])
    answer= 0 
    if(len(set_val)==3): answer= sum(set_val)
    elif(len(set_val)==1) :answer =sum([a,b,c])*sum([a**2,b**2,c**2])*sum([a**3,b**3,c**3])
    else :answer=sum([a,b,c])*sum([a**2,b**2,c**2])
    return answer