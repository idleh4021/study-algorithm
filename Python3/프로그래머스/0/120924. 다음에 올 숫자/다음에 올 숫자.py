def solution(common):
    answer = 0
    if(abs(common[0]-common[1]) == abs(common[1]-common[2])):
        gap = common[1]-common[0]
        answer = common[-1]+gap
    else :
        gap = common[1] / common[0]
        answer = common[-1]*gap
    return answer
