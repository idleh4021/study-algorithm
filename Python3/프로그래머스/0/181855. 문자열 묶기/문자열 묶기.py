def solution(strArr):
    cnt_arr =[len(i) for i in strArr]
    cnt_list = [0]*(max(cnt_arr)+1)
    for c in cnt_arr :
        cnt_list[c]+=1
    
    return max(cnt_list)


