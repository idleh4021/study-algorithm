def solution(n, m, section):
    answer = 0
    while len(section)>0:
        st_val = section[0] # 2
        end_val = st_val + m -1 # 2+4-1
        while len(section)>0 and section[0]<=end_val:
                section.pop(0)
        answer+=1
    return answer