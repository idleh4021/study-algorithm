a,b = map(float,input().split())
c,d = map(float,input().split())
max_v = 0
l = 0 
answer = a/c +b/d
if max_v<answer:
    max_v = answer
    l = 0


answer = c/d+a/b
if max_v<answer:
    max_v = answer
    l = 1

answer = d/b+c/a
if max_v<answer:
    max_v = answer
    l =2


answer = b/a+d/c
if max_v<answer:
    max_v = answer
    l = 3

print(l)
