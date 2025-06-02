L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
days = 0
while A>0 or B>0 :
    days+=1
    A-= C
    B-= D
print(L-days)