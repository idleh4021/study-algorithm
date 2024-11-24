def solution(my_strings, parts):
    answer = []
    for index,s in enumerate(my_strings):
        answer +=s[parts[index][0]:parts[index][1]+1]
    return ''.join(answer)