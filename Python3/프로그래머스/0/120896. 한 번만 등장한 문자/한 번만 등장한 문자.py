def solution(s):
    answer = {}
    list_str = list(s)
    ch_list = set(list_str)
    for c in ch_list:
        answer[c]=list_str.count(c)
    
    return ''.join(sorted(i for i in answer if answer[i]==1))