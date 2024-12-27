def solution(players, callings):
    answer = []
    p_rank = {}
    p_name = {}
    for i in range(len(players)) :
        p_rank[players[i]] = i
        p_name[i]=players[i]
        
    for i in callings:
        rank = p_rank[i]
        p2 = p_name[rank-1]#list(p_rank.keys())[list(p_rank.values()).index(rank-1)]
        p_rank[i]-=1
        p_name[rank-1] = i
        p_rank[p2]+=1
        p_name[rank]=p2
        
    return [i[0] for i in sorted(p_rank.items(), key=lambda x:x[1]) ]
