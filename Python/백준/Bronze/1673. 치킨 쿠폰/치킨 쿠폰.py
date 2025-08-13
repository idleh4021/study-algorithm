import sys

while True:
    input = sys.stdin.readline().rstrip()
    if input == '':
        break
    my_coupon , stampForOnechicken = map(int, input.split())
    myStamp = my_coupon * stampForOnechicken
    chickens = 0

    while myStamp >= stampForOnechicken:
        c = myStamp // stampForOnechicken
        chickens += c
        myStamp = c + (myStamp % stampForOnechicken)

    print(chickens)