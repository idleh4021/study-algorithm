man ,size= map(int, input().split())
size = size*man
arr= map(int, input().split())
answer = [i-size for i in arr]
print(*answer)