def solution(id_pw, db):
    if id_pw in db: return 'login'
    list_db = {}
    for row in db:
        list_db[row[0]] = row[1]
    
    if(list_db.get(id_pw[0])==None) : return 'fail'
    else : return 'wrong pw'
    
    answer = ''
    return answer