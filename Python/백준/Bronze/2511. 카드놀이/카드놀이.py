A = list(map(int,input().split()))
B = list(map(int,input().split()))
last_winner ='D'
a_t_score = 0 
b_t_score = 0
   
for i,v in enumerate(A):
    a_score = v 
    b_score = B[i]
    if a_score==b_score:
       a_t_score+=1
       b_t_score+=1
    elif a_score>b_score:
        a_t_score+=3
        last_winner = 'A'
    else:
        b_t_score+=3
        last_winner ='B'

print(a_t_score,b_t_score)
print('A' if a_t_score>b_t_score else 'B' if b_t_score>a_t_score else last_winner)

