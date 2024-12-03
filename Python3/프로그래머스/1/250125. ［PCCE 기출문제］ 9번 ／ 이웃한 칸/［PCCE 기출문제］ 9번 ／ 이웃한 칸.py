def solution(board, h, w):
    answer = 0
    pt_color = board[h][w]
    tile_list =  GetColor(board,h,w)
    return tile_list.count(pt_color)

def GetColor(board,h,w):
    ps_list =[]
    if not len(board)<=h+1:
        ps_list.append(board[h+1][w])
    if not len(board[h]) <=w+1: 
        ps_list.append(board[h][w+1])
    if not w-1<0:
        ps_list.append(board[h][w-1])
    if not h-1 <0:
        ps_list.append(board[h-1][w])
    return ps_list