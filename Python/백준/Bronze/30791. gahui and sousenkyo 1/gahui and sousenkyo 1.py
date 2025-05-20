arr = list(map(int, input().split()))
arr.sort()
tier1 = arr.pop()
print(len([i for i in arr if abs(i-tier1) <=1000]))