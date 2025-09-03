cups = {1:1,2:0,3:0} # 1 = 컵안의 공

arr = input()
for i in arr:
    if i =='A':
        cups[1],cups[2] = cups[2],cups[1]
    elif i =='B':
        cups[2],cups[3] = cups[3],cups[2]
    else:
        cups[1],cups[3] = cups[3],cups[1]

for i in cups:
    if cups[i] ==1 :
        print(i)
        break