def solution(my_string, indices):
    return ''.join([val for i,val in enumerate(my_string) if i not in indices])