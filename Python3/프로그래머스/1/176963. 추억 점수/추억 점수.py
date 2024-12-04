def solution(name, yearning, photo):
    answer=[]
    map_score = {key: value for key, value in zip(name,yearning)}
    for pic in photo:
        answer.append(sum([map_score[i] for i in pic if i in name]))

    
    return answer