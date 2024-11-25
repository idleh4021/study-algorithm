def solution(my_string, m, c):
    list_ans = []
    for i in range(len(my_string)//m):
        list_ans.append(my_string[i*m:(i+1)*m])
         
     
    return ''.join(i[c-1] for i in list_ans)