from collections import Counter

f,s,t = map(int,input().split())
pay = {1:f,2:s*2,3:t*3}
arr = []

for i in range(3):
    fr,to = map(int,input().split())
    arr += range(fr,to)
    
score = 0 
cnt = Counter(arr)
for i in cnt :
    score += pay.get( cnt.get(i))
print(score)