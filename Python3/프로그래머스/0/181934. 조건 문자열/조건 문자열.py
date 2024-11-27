def solution(ineq, eq, n, m):
    answer= f'{str(n)}{ineq}'+(eq if eq!='!' else '')+str(m)
    return int(eval(answer))