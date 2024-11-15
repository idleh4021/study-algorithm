def solution(hp):
    cnt = hp//5
    hp = hp%5
    cnt += hp//3
    hp= hp%3
    cnt +=hp
    answer = cnt
    return answer