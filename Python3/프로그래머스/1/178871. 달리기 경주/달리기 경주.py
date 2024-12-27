def solution(players, callings):
    answer = []
    p_dic = {}
    for i in range(len(players)) :
        p_dic[players[i]] = i
    
    for i in callings:
        rank = p_dic[i]
        p2 = list(p_dic.keys())[list(p_dic.values()).index(rank-1)]
        p_dic[i]-=1
        p_dic[p2]+=1
        
    return [i[0] for i in sorted(p_dic.items(), key=lambda x:x[1]) ]