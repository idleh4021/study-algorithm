def solution(s):
    candidates=[]
    s= list(s)
    while(len(s) > 0):
        if len(s)==0 :break
        last = s.pop()
        if len(candidates)>0 and candidates[-1]==last:
            candidates.pop()
            continue
        if len(s)==0 : 
            candidates.append(last)
            break 
        last_before = s.pop()
        if last == last_before : continue
        else :
            candidates.append(last)
            if len(s)==0 : 
                
                break
            if(last_before != s[-1]):
                candidates.append(last_before)            
            else :        
                if len(s)>0 : s.pop()
                else: break
    return int(len(s)==0 and len(candidates)==0)
