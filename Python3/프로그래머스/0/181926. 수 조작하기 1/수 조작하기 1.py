def solution(n, control):
    map_control = {'w':1,'s':-1,'d':10,'a':-10}
    for c in control:
        n+=map_control[c]
    return n