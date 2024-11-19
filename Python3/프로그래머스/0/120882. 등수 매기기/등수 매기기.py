def solution(score):
    #등수만 구하면 되므로 평균 필요없음. 총합으로만 rank 처리
    rank = sorted((sum(i) for i in score),reverse=True)
    #**중요**배열에 같은 값이 존재하므로, 앞에있는 인덱스를 불러옴
    return list(rank.index(sum(val))+1 for val in score)

    
    '''
    기존답
    answer = []
    avg_score = []
    rank_num=1
    use_index=[]
    for val in score:
        avg_score.append(sum(val)/2)
    rank = sorted(list(set(avg_score)),reverse=True)
    for i in rank :
        index_list = list(idx for idx,val in enumerate(avg_score) if val==i and idx not in use_index)
        for idx in index_list:
            use_index.append(idx)
            avg_score[idx] = rank_num
        rank_num+=len(index_list)
    return avg_score
    '''