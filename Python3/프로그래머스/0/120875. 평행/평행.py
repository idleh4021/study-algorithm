def solution(dots):
    answer = 0
    list_angle =[]
    case_list = [[1,2,3,4],[1,3,2,4],[1,4,2,3],[2,3,1,4]]
    for i in case_list:
        if(getangle(dots[i[0]-1],dots[i[1]-1])==getangle(dots[i[2]-1],dots[i[3]-1])): return 1
    return 0


def getangle(p1,p2):
    return [(p1[1]-p2[1])/(p1[0]-p2[0])]
