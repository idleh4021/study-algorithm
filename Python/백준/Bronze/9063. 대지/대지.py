cnt = int(input())
x_list=[]
y_list=[]
for i in range(cnt):
    x,y = input().split()
    x_list.append(int(x))
    y_list.append(int(y))
min_x,min_y = min(x_list),min(y_list)
max_x,max_y = max(x_list),max(y_list)
answer= (max_x-min_x)*(max_y-min_y)
print(answer)