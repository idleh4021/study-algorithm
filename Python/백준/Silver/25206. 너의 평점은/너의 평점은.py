scores = {'A+':4.5,'A0':	4.0,'B+':	3.5,'B0':	3.0,'C+':	2.5,'C0':	2.0,'D+':	1.5,'D0':	1.0,'F':0.0}
sum_val = 0
arr = []
for i in range(20):
    s=input()
    t,point,score = s.split()
    if score=='P':continue
    arr.append(float(point)*scores[score])
    sum_val += float(point)

print(sum(arr)/sum_val)