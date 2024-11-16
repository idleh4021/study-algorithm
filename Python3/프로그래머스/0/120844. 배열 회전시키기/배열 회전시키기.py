def solution(numbers, direction):
    answer =[]
    if direction =='right':
        answer.append(numbers[-1])
        for idx,val in enumerate(numbers):
            if idx ==len(numbers)-1 :continue
            answer.append(val)
    else : 
        for idx,val in enumerate(numbers):
            if idx == 0  :continue
            answer.append(val)
        answer.append(numbers[0])
        
        
    
    return answer