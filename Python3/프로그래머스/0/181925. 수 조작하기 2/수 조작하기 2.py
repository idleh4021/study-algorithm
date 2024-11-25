def solution(numLog):
    input_key = {1:'w',-1:'s',10:'d',-10:'a'}
    return ''.join(input_key[numLog[idx+1]-i] for idx,i in enumerate(numLog) if idx<len(numLog)-1)