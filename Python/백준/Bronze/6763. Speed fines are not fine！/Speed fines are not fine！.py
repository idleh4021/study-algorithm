limit =int(input())
speed = int(input())
if speed<=limit:
    print('Congratulations, you are within the speed limit!')
else :
    gap = abs(limit - speed)
    fee = 100 if 1<=gap<=20 else 270 if 21<=gap<=30 else 500
    print(f'You are speeding and your fine is ${fee}.')