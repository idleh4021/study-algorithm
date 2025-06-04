score ={0 : 'E', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D'}
for i in range(3):
    print(score[len([i for i in list(map(int, input().split())) if i==0 ])])