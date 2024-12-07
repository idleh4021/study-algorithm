def solution(foods):
    answer = ''
    foods.pop(0)
    for idx,food in enumerate(foods):
        use_qty =food//2
        answer+=str(idx+1)*use_qty
    answer_right = ''.join(reversed(list(answer)))
    return answer + '0'+answer_right