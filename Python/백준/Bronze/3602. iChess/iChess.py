a,b=map(int,input().split())
a,b = min([a,b]),max([a,b])
all_tiles =a*2
if(a<b): all_tiles+=1
answer= int(all_tiles**0.5)
print('Impossible' if answer ==0 else answer)

