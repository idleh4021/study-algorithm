def solution(rank, attendance):
    candidate_list = [i for idx,i in enumerate(rank) if attendance[idx]]
    ranker= sorted(candidate_list)
    a,b,c, = rank.index(ranker[0]),rank.index(ranker[1]),rank.index(ranker[2])
    return a*10000+b*100+c
