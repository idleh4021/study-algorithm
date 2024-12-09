import math
def solution(number, limit, power):
    answer = []
    
    for target in range(1,number+1):
        val_list =[]
        cnt_list =[]
        cnt=0
        for i in range(int((target)**0.5)):
            if (i+1)*(i+1) == target:
                cnt+=1
            elif target% (i+1) ==0:
                cnt+=2
        
        answer.append(cnt)
            
        
                
    return sum( [i if i<=limit else power for i in answer])