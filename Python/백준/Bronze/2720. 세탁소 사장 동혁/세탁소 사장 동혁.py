cnt = int(input())
coins =[25,10,5,1]
for i in range(cnt):
    answer =[]
    money = int(input())
    for coin in coins:
        answer.append(money//coin)
        money %= coin
    print(' '.join(str(j) for j in answer))
    