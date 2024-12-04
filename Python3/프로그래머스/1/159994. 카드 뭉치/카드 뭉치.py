def solution(cards1, cards2, goal):
    answer = ''
    for val in goal:
        if len(cards1)>0 and cards1[0] == val:
            cards1.pop(0)
            continue
        elif len(cards2)>0 and  cards2[0] == val:
            cards2.pop(0)
            continue
        else : return 'No'
    return 'Yes'
    return answer