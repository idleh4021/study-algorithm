def solution(my_string):
    remove_list = ['a', 'e', 'i', 'o', 'u']
    return ''.join(i for i in my_string if (i not in remove_list))