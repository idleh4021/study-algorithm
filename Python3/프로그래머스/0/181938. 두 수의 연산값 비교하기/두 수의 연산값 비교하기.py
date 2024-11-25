def solution(a, b):
    answer = 0
    return int(f'{a}{b}') if int(f'{a}{b}') > 2*a*b else 2*a*b