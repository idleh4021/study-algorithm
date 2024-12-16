def solution(people,limit):
    answer =0
    people = sorted(people)
    i,j = 0,len(people)-1
    
    if len(people) == 1 : return 1
    while True:
        #if i==len(people) or j<0 :
        if i>j:
            break
        if people[i]+people[j]<=limit:
            answer+=1
            i+=1
            j-=1
            if i ==j :
                answer+=1
                break
            elif i>j :
                break
            else :
                continue
        else :
            answer+= 1
            j-=1
    return answer