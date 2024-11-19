def solution(id_pw, db):
    #dict()를 이용해서 딕셔너리화 개선
    if(dict(db).get(id_pw[0]) == id_pw[1]): return 'login'
    elif(dict(db).get(id_pw[0])==None) : return'fail'
    else : return 'wrong pw'

    ''' 
   기존답
   if id_pw in db: return 'login'
    list_db = {}
    for row in db:
        list_db[row[0]] = row[1]
    
    if(list_db.get(id_pw[0])==None) : return 'fail'
    else : return 'wrong pw'
    
    answer = ''
    return answer
    '''