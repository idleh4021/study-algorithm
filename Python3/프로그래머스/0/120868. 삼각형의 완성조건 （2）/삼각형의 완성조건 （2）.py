def solution(sides):
    answer = 0
    i=1
    while(True):
        if(sides[0]+sides[1]<i):break
        triangle =sorted([sides[0],sides[1],i])
        if(triangle[0]+triangle[1] > triangle[2]): answer+=1
        i+=1
    return answer
