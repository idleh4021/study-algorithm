def solution(my_string):
    my_string = my_string.lower()
    answer = ''.join(sorted([i for i in my_string]))
    return answer