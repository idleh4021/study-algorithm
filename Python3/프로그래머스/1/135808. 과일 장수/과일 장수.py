def solution(k, m, score):
    answer =0 
    score = sorted(score,reverse=True)
    #answer+= sum(score[::m])
    answer = sum(score[m-1::m])*m
    #while len(score)>=m:
    #    answer+= score[:m][-1]*m
    #    score = score[m:]
    return answer