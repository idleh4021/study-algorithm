N,L = map(int, input().split())

lastNum = 1
for i in range(1, N + 1):
    while True : 
        if str(L) in str(lastNum):
            lastNum+=1
            continue
        else :
            lastNum += 1
            break
print(lastNum -1)