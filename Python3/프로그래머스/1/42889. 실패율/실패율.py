def solution(N, stages):
    answer = []
    failed_rate =[]
    stages = sorted(stages,reverse=True)
    a=[]
    b=[]
    dic={}
    sorted_d ={}
    
    for i in range(N):
        if i+1 not in stages : 
            failed_rate.append(0)
            continue
        idx = stages.index(i+1)
        failed_rate.append(stages.count(i+1) /((len(stages[:idx]))+stages.count(i+1)))
    
    
    for index,value in enumerate(failed_rate):
        a.append(index+1)
        b.append(value)
        
    dic = dict(zip(a,b))
    sorted_d = sorted(dic.items(), key =lambda x:x[1],reverse=True )
    for d in sorted_d:
        answer.append(d[0])
    #sorted_ = dict([index+1,val for index,val in enumerate(failed_rate) ])
    
    return answer