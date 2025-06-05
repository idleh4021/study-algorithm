import sys
arr = []
for _ in range(5):
    name = sys.stdin.readline().strip('\n')
    if 'FBI' in name:
        arr.append(_+1)
if len(arr)==0:print('HE GOT AWAY!')
else:print(*arr)
    
