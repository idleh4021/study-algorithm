def solution(rsp):
    answer = ''
    for c in rsp:
        answer+='2' if c=="5"  else '0' if c=='2' else '5'
    return answer