from collections import Counter

answer =0 
a= dict(Counter(input().split()))
if len(a)==1:
    answer = 10000+(1000*int(list(a)[0]))
elif len(a) ==2:
    answer = 1000+(100*(int(max(a, key=a.get))))
else :
    answer = int(max(a.keys()))*100
    
print(answer)