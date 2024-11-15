def solution(money):
    COFFEE = 5500
    answer = [int(money/COFFEE),money%COFFEE]
    return answer
