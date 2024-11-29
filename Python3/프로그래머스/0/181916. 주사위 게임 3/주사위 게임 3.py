import math
from typing import List, Dict
def solution(a, b, c, d):
    set_dice = set([a,b,c,d])
    sorted_list = sorted([a,b,c,d])
    answer =0
    if len(set_dice)==1:
        answer = 1111*a
    elif len(set_dice)==2:

        if sorted_list.count(sorted_list[0]) == 1 or sorted_list.count(sorted_list[0]) == 3:
            p= sorted_list[0] if sorted_list[0]==sorted_list[1] else sorted_list[-1]
            q= sorted_list[0] if sorted_list[0]!=sorted_list[1] else sorted_list[-1]
           # p = sorted_list[0] if sorted_list.count(list[0]) ==3 else sorted_list[-1] 
           # q =sorted_list[-1] if sorted_list.count(list[0]) ==3 else sorted_list[0]
            answer= (10*p+q)**2
        else:
            p,q =sorted_list[0],sorted_list[-1]
            answer = (p+q)*(abs(p-q))
    elif len(set_dice)==3:
        p,q,r=0,0,0
        for i in set_dice:
            if sorted_list.count(i)==2:
                p= i 
                break
        answer = math.prod([i for i in set_dice if i != p])
    else :
        answer = min([a,b,c,d])

    return answer