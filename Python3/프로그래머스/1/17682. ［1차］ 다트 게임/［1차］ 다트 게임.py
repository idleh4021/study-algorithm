def solution(dartResult):
    no_award = dartResult.replace('*','').replace('#','')
    #no_award_list = [no_award[0:2],no_award[2:4],no_award[4:6]]
    no_award_list = no_award.replace('S','S|').replace('D','D|').replace('T','T|').split('|')
    no_award_list.remove('')
    award_list=[]
    i=0
    while(len(dartResult)>0):
        dartResult=dartResult[len(no_award_list[i]):]
        if(len(dartResult)==0): 
            award_list.append('X')
            break
        if dartResult[0] in ['*','#']:
            award_list.append(dartResult[0])
            dartResult = dartResult[1:]
        else: award_list.append('X')
        i+=1
    score_list = [getScore(no_award_list[0]),getScore(no_award_list[1]),getScore(no_award_list[2])]
    for idx,a in enumerate(award_list):
        if a=='X' : continue
        elif a=='*' :
            score_list[idx]=score_list[idx]*2
            if idx>0: score_list[idx-1]=score_list[idx-1]*2
        elif a=='#':
            score_list[idx]*=-1
    answer = 0
    return sum(score_list)

def getScore(str):
    score = int(str[:-1])
    sqr = 1 if str[-1]=='S' else 2 if str[-1]=='D' else 3
    return score**sqr