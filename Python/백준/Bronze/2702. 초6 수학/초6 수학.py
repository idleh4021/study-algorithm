def gcd (a,b):
    if b>a : b,a=a,b
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

def lcm (a,b):
    return (a*b)//gcd(a,b)


n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    print(lcm(a,b),gcd(a,b))