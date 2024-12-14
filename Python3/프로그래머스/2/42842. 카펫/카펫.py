def solution(brown, yellow):
    
    
    prod_val = brown+yellow
    b_val = get_ms_list(prod_val)
    br_val = get_ms_list(brown)
    y_val = get_ms_list(yellow)
    for b in b_val:
        m_list=[i for i in y_val if max(b) > max(i) and min(b)> min(i)+1  ]
        if len(m_list)>0:
            return [max(b),min(b)]
        
    return y_val

def get_ms_list(num):
    answer=[]
    if num==1 :return [[1,1]]
    for i in range(2,int(num**0.5)+2):
        if num%i ==0:
            answer.append([i,num//i])
    return answer