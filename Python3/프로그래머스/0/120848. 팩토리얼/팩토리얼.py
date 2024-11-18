
def solution(n):
    val = 1
    number =1 
    while(n>=val):
        if(n==val): return number
        number+=1
        val*=number
        
    return number-1