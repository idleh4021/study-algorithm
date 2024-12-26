ar=[0]*30
for idx in range(28):
    i =int( input())
    ar[i-1]+=1

minIdx =ar.index(0) 
print(minIdx+1)
print(ar.index(0,minIdx+1)+1)