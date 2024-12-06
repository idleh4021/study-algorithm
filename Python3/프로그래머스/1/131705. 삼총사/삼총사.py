
def solution(number):
    number_list = sorted(number)
    answer = 0
    #for idx,f in enumerate(number_list):
    while(len(number_list)>=3):
        f=number_list.pop(0)
        for s in range(len(number_list)):
            sum = f+number_list[s]
            answer+=len([ i for i in number_list[s+1:] if sum*-1 ==i ])
                
        
        
    return answer
