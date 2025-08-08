def GetNum(c):
    n = ord(c)
    minus_v = 96 if n>90 else 38
    return n-minus_v

def isPrime(n):
    arr =[]
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            arr.append(i)
    return True if len(arr)==0 else False

s = input()
sum_v = sum([GetNum(c) for c in s])
if isPrime(sum_v):
    print('It is a prime word.')
else:
    print('It is not a prime word.')
