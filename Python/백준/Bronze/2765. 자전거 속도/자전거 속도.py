num =1
while True:
    diameter,cycle,sec = map( float,input().split() )
    if(cycle==0):break
    distacne = diameter*3.1415927 * cycle / 12 / 5280
    speed = distacne / sec * 3600
    print(f'Trip #{num}: {distacne:.2f} {speed:.2f}')
    num += 1
