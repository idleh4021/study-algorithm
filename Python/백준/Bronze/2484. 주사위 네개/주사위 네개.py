import collections
answer = [] 
for _ in range(int(input())):
    arr = sorted(list(map(int,input().split())))
    length = len(set(arr))
    if length ==1:
        answer.append(50000+arr[0]*5000)
    elif length ==4:
        answer.append(arr[-1]*100)
    elif length ==2:
        s = list(set(arr))
        if arr[0]==arr[1] and arr[2]==arr[3]:
            answer.append(2000+s[0]*500+s[1]*500)
        else:
            if arr[0]!=arr[1]:
                answer.append(10000+arr[-1]*1000)
            else:
                answer.append(10000+arr[0]*1000)
    else :
        dic = collections.Counter(arr)
        answer.append(1000+[i for i in dic if dic[i]==2][0]*100)
print(max(answer))