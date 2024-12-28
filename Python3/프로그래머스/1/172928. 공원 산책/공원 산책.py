def solution(park, routes):
    answer = []
    pos = []
    y = len(park)
    x = len(park[0])
    for i in range(len(park)):
        if 'S' in park[i]:
            pos = [i,park[i].index('S')]
            break
        
    for i in routes:
        op,n = i.split()
        
        temp_pos = pos.copy()
        can_move = True
        for i in range(int(n)):
            if op=='E':
                temp_pos[1]+=1
                if temp_pos[1] >=x or park[temp_pos[0]][temp_pos[1]] == 'X':
                    can_move=False
                    break
            elif op=='W':
                temp_pos[1]-=1
                if temp_pos[1] <0 or park[temp_pos[0]][temp_pos[1]] == 'X':
                    can_move=False
                    break
            elif op=='S':
                temp_pos[0]+=1
                if temp_pos[0] >=y or park[temp_pos[0]][temp_pos[1]] == 'X':
                    can_move=False
                    break
            elif op=='N':
                temp_pos[0]-=1
                if temp_pos[0] <0 or park[temp_pos[0]][temp_pos[1]] == 'X':
                    can_move=False
                    break
        if can_move:
            pos=temp_pos
    return pos