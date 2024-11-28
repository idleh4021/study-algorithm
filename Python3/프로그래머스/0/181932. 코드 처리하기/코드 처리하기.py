def solution(code):
    mode=0
    ret =[]
    for i in range(len(code)):
        if(mode) : #1
            if code[i] != '1' and i%2==1 : 
                ret.append(code[i])
            elif code[i]== '1' : mode =0
        else : #0
            if code[i] != '1' and i%2==0 : 
                ret.append(code[i])
            elif code[i]== '1' : mode =1
    return ''.join(ret) if len(ret)>0 else 'EMPTY'