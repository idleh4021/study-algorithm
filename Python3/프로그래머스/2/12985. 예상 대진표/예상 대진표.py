import math
def solution(n,a,b):
 #   answer = int(math.log2(b if b%2==0 else b+1))#,int(math.log2(a if a%2==0 else a+1))
    answer =0 
    if n==2 : return 1
    while True:
        a = math.ceil((a if a%2!=0 else a-1 )/2)
        b = math.ceil((b if b%2!=0 else b-1 )/2)
        answer+=1
        if a==b :
            break
    return answer