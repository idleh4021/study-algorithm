import sys
N,C = map(int, sys.stdin.readline().split())
interval = []
fireworks = {}
answer = 0 

for i in range(1, N + 1):
    interval.append(int(sys.stdin.readline()))

interval.sort()
for s_idx,i in enumerate(interval):
    if i== 0 : continue
    for e_idx in range(s_idx+1,len(interval)):
        v = interval[e_idx]
        if v ==0: continue
        if v % i == 0 :
            interval[e_idx] = 0
interval = list(filter(lambda x: x != 0, interval))
    
for inter in interval:
    i = 1
    while True:
        firework = i * inter
        if(i * inter > C):
            break
        fireworks[firework] = fireworks.get(firework,0)+1
        i+=1

print(len(fireworks))
    


# def lcm (a,b):
#     return a*b // gcd(a,b)

# def gcd(a,b):
#     if(a%b ==0):
#         return b
#     return gcd(b, a%b)

