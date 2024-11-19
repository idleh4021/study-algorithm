import math
def solution(balls, share):
    #참고용 답
    return math.comb(balls,share)
    '''
    기존답
    list_up = list(range(balls-share+1,balls+1))
    list_down = list(range(1,share+1))
    
    for i in list_down:
        if(i in list_up):
            list_up.remove(i)
            list_down.remove(i)
            
    answer_up = 1
    answer_down = 1
    for i in list_up:
        answer_up*=i
    for j in list_down:
        answer_down *=j
    return answer_up//answer_down
    '''
    