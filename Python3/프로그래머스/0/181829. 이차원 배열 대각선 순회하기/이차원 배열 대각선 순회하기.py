def solution(board, k):
    answer= 0
    for idx,row in enumerate(board):
        answer += sum(v for v_idx,v in enumerate(row) if idx+v_idx<=k)
            
    return answer