points = 5
idx = int(input())
gap = 7

for _ in range(1,idx):
    points += gap
    gap+=3
print(points%45678)