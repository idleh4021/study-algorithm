me =list( map(int,input().split()))
sec = int(input())
d = input()
target = [0,0]
direction = {'I':[1,0],'S':[0,1],'Z':[-1,0],'J':[0,-1]}
arr=[]
i =0
if abs(me[0]-target[0])<=1 and abs(me[1]-target[1])<=1:
    arr.append(i)
for c in d:
    i+=1
    target[0]+=direction[c][0]
    target[1]+=direction[c][1]
    if abs(me[0]-target[0])<=1 and abs(me[1]-target[1])<=1:
        arr.append(i)
if(len(arr)==0):print('-1')
else:
    for i in arr:
        print(i)