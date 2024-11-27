def solution(str_list):
    l,r =0,0  
    l,r=str_list.index('l') if 'l' in str_list else 999,str_list.index('r') if 'r' in str_list else 999
 
    return str_list[:l] if l<r else str_list[r+1:] if l>r else []