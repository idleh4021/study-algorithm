def solution(k, tangerine):
    answer = 0
    t = [0]*(max(set(tangerine)))
    
    for i in tangerine:
        t[i-1] +=1
        
    t = sorted(t)
    while True:
        v = t.pop()
        answer+=1
        k-=v
        if k<=0:
            break
    return answer