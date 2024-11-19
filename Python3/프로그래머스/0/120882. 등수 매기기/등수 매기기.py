def solution(score):
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