def solution(lines):
    answer=0
    list_line = []

    for line in lines:
        line_arr = list(range(min(line),max(line)+1))
        #list_line+=line_arr
        list_line.append(line_arr)

    com_line=[]
    arr_1 =list(set(list_line[0])&set(list_line[1]))
    if(len(arr_1)>1):  com_line.append(arr_1)
    arr_2=list(set(list_line[0])&set(list_line[2]))
    if(len(arr_2)>1):  com_line.append(arr_2)
    arr_3 = list(set(list_line[1])&set(list_line[2]))
    if(len(arr_3)>1):  com_line.append(arr_3)
    
    if(len(com_line)==0):return 0
    if(len(com_line)==1) : return max(com_line[0])- min(com_line[0])
    elif(len(com_line)==2) : 
        hap = set(com_line[0])|set(com_line[1])
        if(len(hap)==0): 
            return getlength(com_line[0])+getlength(com_line[1])
        elif(len(set(com_line[0])&set(com_line[1]))==0): return getlength(com_line[0])+getlength(com_line[1])
        else:  return getlength(hap)
    else:
        answer=0
        hap_1 = set(com_line[0])|set(com_line[1])
        hap_2 = set(com_line[1])|set(com_line[2])
        if(len(hap_1)>0 and len(hap_2)>0):
            hap_3 =  hap_1 | hap_2
            if(len(hap_3)>0): return getlength(hap_3)
            else :return getlength(hap_1) +getlength(hap_2)
        if(len(hap_1)>0): answer+= getlength(hap_1)
        else : answer+=getlength(com_line[0])+getlength(com_line[1])
        if(len(hap_2)>0): answer+= getlength(hap_2)
        else : answer+=getlength(com_line[1])+getlength(com_line[2])
        return answer
    


def getlength(list):
    return max(list)- min(list)


