def solution(n):
    location=[0,0]
    curr = 'r'
    dir = {'u':[-1,0],'d':[1,0],'l':[0,-1],'r':[0,1]}
    answer = []
    for _ in range(n):
        answer.append([0] * n)
    for i in range(1,n**2+1):
            answer[location[0]][location[1]] =i
            
            iszero = nextIsZero(answer,location[0]+dir[curr][0],location[1]+dir[curr][1])
            if curr=='r' and (location[1]+dir[curr][1] >= len(answer[0]) or not iszero) : 
                curr='d'
            elif curr=='d' and (location[0]+dir[curr][0] >= len(answer)or not iszero):
                curr='l'
            elif curr=='l' and (location[1]+dir[curr][1] <0 or not iszero):
                curr='u'
            elif curr=='u' and (location[0]+dir[curr][0] <0 or not iszero):
                curr='r'
            location[0],location[1] = location[0]+dir[curr][0],location[1]+dir[curr][1]
    
        
    return answer

def nextIsZero(answer,a,b):
    result = True
    try:
        result=answer[a][b]==0
    except:
        result=False
        return result
    return result