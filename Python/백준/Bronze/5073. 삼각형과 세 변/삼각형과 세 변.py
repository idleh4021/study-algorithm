
while True:
    anaswer=''
    lines = input().split()
    lines = sorted([int(i) for i in lines])
    if lines[0]==lines[1] and lines[1]==lines[2]:
        if lines[0]==0:break
        else: print('Equilateral')
    elif lines[0]+lines[1]<=lines[-1]: print('Invalid')
    elif lines[0]!= lines[1] and lines[1]!=lines[2] and lines[0]!=lines[2]:print('Scalene')
    else : print('Isosceles')    