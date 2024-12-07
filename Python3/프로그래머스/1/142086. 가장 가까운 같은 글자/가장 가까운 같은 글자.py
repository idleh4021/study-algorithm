def solution(s):
    answer = []
    arr = list(s)
    for idx,c in enumerate(arr):
        find_list = [val for i_idx,val in enumerate(arr) if i_idx != idx and idx>=i_idx] 
        if(c not in find_list):
            answer.append(-1)
            continue
        cnt = 1
        for i,val in enumerate(find_list[::-1]):
            
            if(val==c) : 
                answer.append(abs(cnt))
                break
            cnt+=1
        #result = min([abs(i-idx) for i,val in enumerate(find_list) if val ==c])
        #answer.append(result)
    return answer