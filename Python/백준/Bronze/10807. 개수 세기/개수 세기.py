from collections import Counter
input()
a= dict(Counter(input().split(' ')))
find_val = input()
print(a[find_val] if find_val in a else 0 )