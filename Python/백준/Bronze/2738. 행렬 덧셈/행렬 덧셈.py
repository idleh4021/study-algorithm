r,c = input().split()
r = int(r)
c= int(c)
a = [[0]*c for i in range(r)]


for i in range(r):
    c_list = input().split()
    for j in range(len(c_list)):
        a[i][j] += int(c_list[j])
for i in range(r):
    c_list = input().split()
    for j in range(len(c_list)):
        a[i][j] += int(c_list[j])

for i in a:
    print(' '.join([str(j) for j in i]))