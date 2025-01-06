def getCol(num):
    is_odd = True
    result = 1
    answer = [1]
    gap=4
    while True:
        if is_odd :
            result+=1
            answer.append(result)
            if num>=answer[-2] and num<=answer[-1] :
                break
                #return len(answer)-1
            is_odd=False
        else :
            result+=gap
            gap+=4
            answer.append(result)
            if num>=answer[-2] and num<=answer[-1] :
                break
                #return len(answer)-1
            is_odd=True
    return answer

get_num = int(input())
cols = getCol(get_num)
col = cols[-2]
idx = len(cols)-1
mom =0
son = 0
if cols[-1]-cols[-2]==1:
    if cols[-1]==get_num:
        mom = len(cols)
        son = 1
    elif cols[-2] == get_num:
        mom = idx
        son =1
    else:
        mom = idx - abs(get_num-col+1)
        son = idx + abs(get_num-col+1)
else :
    if abs(col-get_num)>idx:
        mom = abs(get_num-col-idx+1)
        son = idx+1 -abs(get_num-col-idx)
    elif abs(col-get_num)==idx:
        son = len(cols)#cols[-1]
        mom =1
    elif abs(col-get_num)==0:
        mom = idx#cols[-2]
        son =1
    else : #abs(col-get_num)<idx:
        mom = idx - abs(get_num-col)
        son = 1 + abs(get_num-col)
    
print(str(son)+'/'+str(mom))