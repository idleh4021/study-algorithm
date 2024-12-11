def solution(s):
    s_list = [int(i) for i in s.split(' ')]
    return f'{min(s_list)} {max(s_list)}'