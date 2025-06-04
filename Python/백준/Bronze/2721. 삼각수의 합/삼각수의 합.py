def T(n):
    return sum(list(range(1,n+1)))
def W(k):
    answer =0 
    for i in range(1, k+1):
        answer += i*T(i+1)
    return answer

t = int(input())
for _ in range(t):
    a= W(int(input()))
    print(a)
    