def solution(my_string):
    list_string = my_string.split(' ')
    answer =int(list_string[0])
    while(len(list_string)!=1):
        if list_string[1] =='+':
            answer += int(list_string[2])
        else :
            answer -= int(list_string[2])
        list_string = list_string[2:]
            
    return answer