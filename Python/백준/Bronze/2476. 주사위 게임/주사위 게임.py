import sys
score = []
for _ in range(int(input())):
    dice = list(map(int,sys.stdin.readline().strip('\n').split()))
    dice = sorted(dice)
    if(dice[0]==dice[1]==dice[2]):
        score.append(10000+(dice[0]*1000))
    elif(dice[0]==dice[1] or dice[1]==dice[2]):
        score.append(1000+(dice[0] if dice[0]==dice[1] else dice[1] *100))
    else : score.append(max(dice)*100)
print(max(score))