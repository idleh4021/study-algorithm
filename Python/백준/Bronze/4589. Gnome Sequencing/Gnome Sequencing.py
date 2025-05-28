"""
Gnomes:
Ordered
Unordered
Ordered
"""
cnt = int(input())
print('Gnomes:')
for _ in range(cnt):
    arr = list(map(int,input().split()))
    if arr == sorted(arr) or arr == sorted(arr,reverse=True):
        print("Ordered")
    else :
        print("Unordered")
