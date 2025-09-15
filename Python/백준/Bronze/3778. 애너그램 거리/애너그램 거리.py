import sys
import collections
for _ in range(int(sys.stdin.readline())):
    gap = 0
    a = sys.stdin.readline()
    b=  sys.stdin.readline()
    a_cnt = collections.Counter(a)
    b_cnt = collections.Counter(b)
    for k in a_cnt:
        gap += abs(a_cnt.get(k,0) - b_cnt.get(k,0))
        if k in b_cnt: b_cnt.pop(k)
    for k in b_cnt:
        gap += b_cnt[k]
    
    print(f'Case #{_+1}: {gap}')
  