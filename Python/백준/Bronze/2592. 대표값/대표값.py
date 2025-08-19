import sys
arr = []
for _ in range(10):
    arr.append(int(sys.stdin.readline().strip()))
print(sum(arr) // 10)
max_cnt = 0
max_num = 0
for i in set(arr):
    cnt = arr.count(i)
    if cnt > max_cnt:
        max_cnt = cnt
        max_num = i
print(max_num)
