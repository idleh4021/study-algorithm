from collections import Counter
x_list = []
y_list = []
answer_x=0
answer_y =0
for i in range(3):
    x,y =input().split()
    x_list.append(int(x))
    y_list.append(int(y))

count_x = Counter(x_list)
count_y = Counter(y_list)

for i in count_x:
    if count_x[i]==1:
        answer_x = i
        break
for i in count_y:
    if count_y[i] ==1:
        answer_y = i

print(f'{answer_x} {answer_y}')
        