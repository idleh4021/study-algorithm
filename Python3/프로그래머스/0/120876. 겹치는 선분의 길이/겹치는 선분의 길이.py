def solution(lines):
    list_line = []
    for line in lines:
        line_arr = list(range(line[0],line[1]+1))
        list_line+=line_arr
        #list_line.append(line_arr)
    list_value = list(i for i in set(list_line) if len([j for j in list_line if j==i])>1)
    cnt = 1
    for idx in range(1,len(list_value)):
        if(abs(abs(list_value[idx])-abs(list_value[idx-1]))==1) :cnt+=1
    answer = cnt-1
    return answer
