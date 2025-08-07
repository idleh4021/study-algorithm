import sys
import time
import math
T = int(sys.stdin.readline())

def GetCountLastZero(val,base):
    result = 0
    while val%base== 0:
        result+=1
        val = val//base
    return result

def getTryNums(N):
    result = set()
    for i in range(1,int(N**0.5)+1):
        if N % i ==0:
            result.add(i)
            #result.add(N//i)
    return result
        

for _ in range(T):
    answer = 0
    N = int(sys.stdin.readline())
    #st= time.perf_counter()
    arr = getTryNums(N) # 약수
    # ed= time.perf_counter()
    # print(f'{ed-st:.10f} sec')
    for base in arr : 
        if base == 1 : continue
        answer += GetCountLastZero(N,base)
    answer +=len(arr)- (1 if(N**0.5)%1 ==0 else 0)
    print(answer)
    