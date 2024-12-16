def solution(people, limit):
    answer = 0
    people = sorted(people)
    while len(people)>0:
        if(len(people)==1):
            answer+=1
            break
        man = people.pop()
        if man ==limit or limit-man <40:
            answer+=1
            continue
        gap = limit-man
        if gap in people :
            #people.remove(gap)
            del people[people.index(gap)]
            answer+=1
        else :
            if abs(limit-people[0])<abs(limit-people[-1]):
                del people[0]
                answer+=1
            elif abs(limit-people[0])>=abs(limit-people[-1]) :
                people.pop()              
                answer+=1
            else : answer+=2
            
    return answer