def getDistance(x,y):
    return ((x**2 if x!= 0 else 0) + (y**2 if y != 0 else 0))**0.5

def getScore(distance):
    if 0<=distance<=3: return 100
    elif 3<distance<=6: return 80
    elif 6<distance<=9: return 60
    elif 9<distance<=12: return 40
    elif 12<distance<=15: return 20
    else: return 0
        

for _ in range(int(input())):
    scores = []
    arr = list(map(float,input().split()))
    for idx in range(len(arr)//2):
        x = arr[idx*2]
        y = arr[idx*2+1]
        scores.append(getScore(getDistance(abs(x),abs(y))))
    p1 = sum(scores[:3])
    p2 = sum(scores[3:])
    
    print(f'SCORE: {p1} to {p2},', end = ' ')
    if p1==p2 : print("TIE.")
    elif p1>p2 : print('PLAYER 1 WINS.')
    else : print('PLAYER 2 WINS.')
        

