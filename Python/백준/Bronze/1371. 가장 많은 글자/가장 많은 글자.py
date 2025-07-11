import sys

ans = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

data = sys.stdin.read()  # EOF까지 한 번에 입력 받음

for c in data:
    if c.isalpha():
        ans[c.lower()] += 1

max_val = max(ans.values())
print(''.join([k for k in ans if ans[k] == max_val]))