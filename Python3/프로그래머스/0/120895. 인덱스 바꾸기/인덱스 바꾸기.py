def solution(my_string, num1, num2):
    list_string = list(my_string)
    tmp_string = list_string[num1]
    tmp_string2 = list_string[num2]
    list_string[num1]= tmp_string2
    list_string[num2] = tmp_string
    return ''.join(list_string)