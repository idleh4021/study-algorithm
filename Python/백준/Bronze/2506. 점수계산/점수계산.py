cnt = int(input())
ox = map(int,input().split())
score=0
ans = 0
for i in ox:
    if(i ==1):
        score+=1
        ans += score
    else : score = 0
print(ans)