def solution(babbling):
    can_say = ['aya','ye','woo','ma']
    answer = 0
    for i in babbling:
        while(True):
            if i.startswith('aya') :
                i =i[3:]
                if i.startswith('aya') : break
                continue
                #can_say.remove('aya')
            elif i.startswith('woo'):
                i =i[3:]
                if i.startswith('woo'): break
                continue
            
                #can_say.remove('moo')
            elif i.startswith('ye'):
                i = i[2:]
                if i.startswith('ye'): break
                continue
                #can_say.remove('ye')
            elif i.startswith('ma'):
                i = i[2:]
                if i.startswith('ma'): break
                continue
                #can_say.remove('ma')
            
            if len(i)==0 : answer+=1
            
            break
    return answer    