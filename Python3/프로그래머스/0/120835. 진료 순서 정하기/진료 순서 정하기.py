def solution(emergency):
    rank_list = sorted(emergency)    
    answer = [len(rank_list)-rank_list.index(i) for i in emergency]
    return answer