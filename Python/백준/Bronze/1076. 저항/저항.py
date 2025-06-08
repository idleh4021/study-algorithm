import sys
res={'black':0,
     'brown':1,
     'red':2,
     'orange':3,
     'yellow':4,
     'green':5,
     'blue':6,
     'violet':7,
     'grey':8,
     'white':9}

c1 = sys.stdin.readline().strip('\n')
c2= sys.stdin.readline().strip('\n')
c3 = sys.stdin.readline().strip('\n')

answer = int(str(res[c1])+str(res[c2]))*(10**res[c3])
print(answer)

