def solution(numbers):
    numbers.sort()
    a = numbers[0]*numbers[1]
    b = numbers[-1]*numbers[-2]
    return a if a>b else b