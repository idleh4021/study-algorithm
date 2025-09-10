#print((1,2,2)==(2,2,1))

def getDiv(n):
    arr = [] 
    for i in range(1,int(n**0.5)+1):
        if n% i == 0 : arr.append(i)
    return arr

def getSurface(arr):
    result = {}
    for i in arr:
        a,b,c = i[0],i[1],i[2]
        answer = ((a*b)+(b*c)+(a*c))*2
        result[(a,b,c)]= answer
    return result

def gap(dic):
    result = {}
    for i in dic:
        result[tuple(i)] = abs(i[0]-i[1])+abs(i[1]-i[2])
    return result

n = int(input())
#n = 1000000
arr = [] 
lst = []
arr.extend(getDiv(n))
answer ={}
for i in arr:
    a = i
    b = n//a
    c_list = getDiv(b)
    lst.extend([[a,j,int(b//j)] for j in c_list])
    c_list2= getDiv(a)
    lst.extend([[j,b,int(a//j)] for j in c_list2])
    #answer=getSurface(lst)
    answer = gap(lst)
#print(*arr)
#print(answer)
print(*min(answer,key=answer.get))
#print(*min(answer, key=answer.get))
    
