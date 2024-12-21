def solution(X, Y):
    answer = '-1'
    X = sorted(X);
    Y= sorted(Y);
    num_X = {}
    num_Y = {}
    answer_list = []
    for i in range(10):
        str_num = str(i)
        num_X[str_num] = X.count(str_num)
        num_Y[str_num] = Y.count(str_num)
            
    for i in sorted(num_X,reverse=True):
        while True:
            if num_X[i]==0: break
            if num_Y[i]==0: break
            answer_list.append(i)
            if i=='0' and answer_list[0]=='0' : break
            num_X[i]-=1
            num_Y[i]-=1
            
    
    return answer if len(answer_list)==0 else ''.join(answer_list)
