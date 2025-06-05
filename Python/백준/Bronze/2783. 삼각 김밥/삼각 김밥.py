price=[]
won,g = map(float, input().split())
price.append(won/g*1000)
for i in range(int(input())):
    won, g = map(float, input().split())
    price.append(won/g*1000)
print(f'{min(price):.2f}')

