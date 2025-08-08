N = input()
s=''
idx = 0
i =1
while True:
    s+=str(i)
    if N in s:
        idx +=s.find(N)
        break
    if len(s)> len(N)*2:
        s = s[len(N):]
        idx += len(N)
    i+=1
print(idx+1)
        