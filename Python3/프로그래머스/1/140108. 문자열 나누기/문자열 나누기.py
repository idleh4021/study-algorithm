def solution(s):
    answer = 0
    x=''
    x_cnt =0 
    not_x_cnt = 0
    
    for idx,i in enumerate(s) :
        if x =='' : x=i
        if x==i:
            x_cnt +=1
        else :
            not_x_cnt+=1
        if x_cnt == not_x_cnt:
            answer+=1
            x_cnt = 0
            not_x_cnt=0
            x=''
        if idx==len(s)-1 and x!= '':
            answer+=1 
            break
    return answer