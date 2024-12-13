def solution(s):
    answer =[]
    for i in s:
        if len(answer)==0:
            answer.append(i)
        elif i == answer[-1]:
            answer.pop()
        else : 
            answer.append(i)          

    return int(len(answer)==0)