def solution(s1, s2):
    answer = len([i for i in s1 if i in s2])
    return answer