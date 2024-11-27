def solution(my_string):
    # a 97 A 65 z 122 Z 90
    answer = [0] * 52
    for c in my_string:
        asc = ord(c)
        if asc <97:
            answer[asc-65]+=1
        else :
            answer [asc-71]+=1
            
    return answer