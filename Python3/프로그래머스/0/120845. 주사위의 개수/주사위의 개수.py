def solution(box, n):
    layer = box[2] // n
    height = box[1] // n 
    width = box[0] // n
    answer = layer * height * width
    return answer