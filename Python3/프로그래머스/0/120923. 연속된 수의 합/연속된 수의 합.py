def solution(num, total):
    numbers = sum(list(range(1,num)))
    x = (total-numbers)//num
    
    return list(range(x,x+num))