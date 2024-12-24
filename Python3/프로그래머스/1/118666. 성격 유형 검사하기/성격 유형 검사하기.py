f={'R':0,'T':0}
s= {'C':0,'F':0}
t={'J':0,'M':0}
fo={'A':0,'N':0}
def solution(survey, choices):
    answer =''

    for idx,val in enumerate(survey):
        if choices[idx] >4 :
            getloc(val)[val[1]] += choices[idx]-4
        elif choices[idx]==4: 
            continue
        else :
            getloc(val)[val[0]] += choices[idx] if choices[idx]==2 else 1 if choices[idx] == 3 else 3 
    answer += getstrMax(f)
    answer += getstrMax(s)
    answer += getstrMax(t)
    answer += getstrMax(fo)
    
    return answer

def getloc(val):
    answer= {}
    
    if val[0] in f:
        return f
    elif val[0] in s:
        return s
    elif val[0] in t:
        return t
    else:
        return fo    
    
def getstrMax(t):
    scores = [t[i] for i in t]
    if scores[0]==scores[1]:
        return sorted(i for i in t)[0]
    else:
        return max(t,key=t.get)
    