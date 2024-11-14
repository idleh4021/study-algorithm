def solution(my_string, overwrite_string, s):
    answer =''
    list_str = list(my_string)
    for idx,c in enumerate(list(my_string)):
        
        if idx>=s and idx<s+len(overwrite_string):
            list_str[idx]=overwrite_string[idx-s]
        else: continue
            
    answer = ''.join(list_str)
    return answer
    