def solution(my_string):
    answer = ''.join([' ' if not i.isdigit() else i for i in my_string]).split(' ')
    return sum([int(i) for i in answer if i.isdigit()])