def solution(keyinput, board):
    key_value = {'up':[0,1],'down':[0,-1],'left':[-1,0],'right':[1,0]}
    x,y=0,0
    for key in keyinput:
        x=x+key_value[key][0]  if abs(x+key_value[key][0])<=(board[0]-1)//2 else x
        y=y+key_value[key][1] if abs(y+key_value[key][1])<=(board[1]-1)//2 else y
    answer = [x,y]
    return answer
