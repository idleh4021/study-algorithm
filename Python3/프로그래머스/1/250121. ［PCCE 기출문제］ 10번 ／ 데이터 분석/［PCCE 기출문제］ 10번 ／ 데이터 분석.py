def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    exts={'code':0, 'date':1,'maximum':2,'remain':3}
    answer = [i for i in data if i[exts[ext]]<val_ext]
    answer.sort(key=lambda x:x[exts[sort_by]])
    return answer