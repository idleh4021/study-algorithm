import sys
arr =[] 
answer =0
n = int(sys.stdin.readline().strip())
cnt = 0
A = None
#F = None
while True: 
    val = sys.stdin.readline().strip()
    if val in ('+','-','*','/'):
        if(val in ['*','/']):
            B = int(sys.stdin.readline().strip())
            cnt+=1
            A = A*B if val =='*' else A//B 
        else:
            if A !=None:
                arr.append(A)
                arr.append(val)
                A=None
    else:
        if A ==None: A = int(val)
        else : arr.append(val)
        cnt+=1
    if cnt == n:
        arr.append(A)
        break
if(len(arr) == 1):print(arr[0])
else:
    answer = arr.pop(0)

while len(arr) !=0:
    F = arr.pop(0)
    B =int(arr.pop(0))
    answer = answer + B*(1 if F =='+' else -1)
print(answer)