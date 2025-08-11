start,end = sorted(map(int,input().split()))
if start == end : 
    print(start)
    exit()
total_times = end-start+1
times= total_times //2 
val = end+start
if val ==0:
    print(0)
    exit()
# 씨바 = ((start+end)//2 if times%2 ==0 else 0) 
# 아니씨바 = val*times
print(val*times+((start+end)//2 if total_times%2 !=0 else 0) )
