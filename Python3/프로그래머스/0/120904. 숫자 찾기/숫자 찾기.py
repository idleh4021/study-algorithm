def solution(num, k):
    answer = -1
    for val in str(num):
        if(val == str(k)):
            answer =list(str(num)).index(str(k))+1
            break   
    return answer
    