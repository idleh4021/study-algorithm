def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if(len(str(i).replace('5','').replace('0',''))==0):answer.append(i)
    return answer if len(answer)>0 else [-1]