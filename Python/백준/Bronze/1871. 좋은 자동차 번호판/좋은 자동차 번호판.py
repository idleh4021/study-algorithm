N = int(input())

def GetFScore(f):
    reverse_f = f[::-1]
    answer= 0
    for i,c in enumerate(reverse_f):
        c_num = ord(c) - ord('A')
        answer += c_num * (26 ** i)
    return answer


for _ in range(N):
   f,s = input().split('-')
   f_score = GetFScore(f)
   s_score = int(s)
   if abs(f_score - s_score) <= 100:
       print('nice')
   else:
       print('not nice')
    
    