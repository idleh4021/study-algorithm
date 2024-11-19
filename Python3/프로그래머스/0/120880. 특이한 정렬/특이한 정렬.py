def solution(numlist, n):
    gap_list = [abs(i-n) for i in numlist]
    min_list = sorted(set(gap_list))
    answer = [ ]
    for i in min_list :
        index_list = [ index for index,val in enumerate(gap_list) if i==val]
        num_sorted = sorted([numlist[val] for val in index_list],reverse=True)
        answer+=num_sorted
    
    
    return answer