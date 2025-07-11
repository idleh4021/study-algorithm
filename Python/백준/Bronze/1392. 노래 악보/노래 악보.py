N ,Q = map(int, input().split())
arr = []
for c in range(N):
    #arr.append([(c+1)] *int(input()) )
    arr += [(c+1)] * int(input())
for q in range(Q):
    print(arr[int(input())])