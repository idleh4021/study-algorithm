Adrian = 'ABC'
Bruno = 'BABC'
Goran ='CCAABB'
N = int(input())
s = input()

arr = {'Adrian':0,'Bruno':0,'Goran':0}

for idx,c in enumerate(s):
    if Adrian[idx%len(Adrian)] == c : arr['Adrian']+=1
    if Bruno[idx%len(Bruno)] == c : arr['Bruno']+=1
    if Goran[idx%len(Goran)] == c : arr['Goran']+=1

max_val = max(arr.values())
print(max_val)
for i in arr:
    if max_val == arr[i]:print(i)
    


