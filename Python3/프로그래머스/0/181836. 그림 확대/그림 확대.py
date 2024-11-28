def solution(picture, k):
    answer = []
    for i in picture:
        for cnt in range(k):
            answer.append(''.join([c*k for c in i]))
    
    return answer