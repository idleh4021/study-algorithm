def solution(s):
    answer = True
    open_case =0
    
    for i in s:
        if i==')':
            if open_case ==0: return False
            else : open_case-=1
        else :
            open_case+=1
    
    return True if open_case==0 else False
