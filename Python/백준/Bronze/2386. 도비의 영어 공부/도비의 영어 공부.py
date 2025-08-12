while True:
    arr = input().split()
    key = arr.pop(0)
    if(key=="#") : break
    answer = 0
    for s in arr:
        answer += len([i for i in s if i.lower()==key])
    print(key,answer)

