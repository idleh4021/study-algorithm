def solution(babbling):
    sounds=["aya", "ye", "woo", "ma"]
    answer = 0
    for bab in babbling:
        for sound in sounds:
            bab=bab.replace(sound,'1')
        if(len(bab.replace('1',''))==0): answer+=1

    return answer
