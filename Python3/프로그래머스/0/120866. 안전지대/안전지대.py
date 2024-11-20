def solution(board):
    for y_idx,line in enumerate(board):
        mine_list = [index for index,mine in enumerate(line) if mine ==1]
        if(len(mine_list)==0):continue
        y_index = [y_idx-1,y_idx,y_idx+1]
        x_index = [[x_idx-1,x_idx,x_idx+1] for x_idx in mine_list]
        for y in y_index:
            if y<0 or y>len(board)-1 : continue
            for x_list in x_index:
                for x in x_list:
                    if(x<0 or x>len(board)-1) : continue
                    if(y_index.index(y)==1 and x_list.index(x)==1):continue
                    board[y][x] = 2 if board[y][x]!=1 else 1
            
    answer = sum((i.count(0) for i in board))
    return answer