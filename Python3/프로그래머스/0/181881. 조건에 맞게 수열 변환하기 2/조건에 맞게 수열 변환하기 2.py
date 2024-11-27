def solution(arr):
    x=0
    x1 = arr
    x2 = []
    while(True):
        x2 = [i//2 if i>=50 and i%2==0 else i*2+1 if i<50 and i%2==1 else i  for i in x1]   
        if(x1==x2) : break
        else : x1=x2
        x+=1 
    return x