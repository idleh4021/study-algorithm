def solution(s):
    answer = ''.join([i.upper() if idx==0 or s[idx-1]==' ' else i.lower() for idx,i in enumerate(s) ])
    return answer