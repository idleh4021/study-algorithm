def solution(k, score):
    answer = []
    board =[]
    for i in score:
        board.append(i)
        if(len(board)>k):
            board= sorted(board,reverse=True)[:k]
        answer.append(min(board))
    return answer