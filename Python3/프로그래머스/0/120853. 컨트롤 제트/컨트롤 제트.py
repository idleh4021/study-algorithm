def solution(s):
    list_s = s.split()        
    answer =0
    for index,val in enumerate(list_s):
        try: answer+=int(val)
        except: answer+= -1*(int(list_s[index-1]))
    return answer
    