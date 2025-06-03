import sys
cnt = int(sys.stdin.readline().strip('\n'))
arr = map(int,sys.stdin.readline().strip('\n').split())
y_sum=0
m_sum=0
for i in arr:
    y_sum += ((i//30)+1)*10
    m_sum += ((i//60)+1)*(15)
print('Y' if m_sum>y_sum else 'M' if y_sum>m_sum else 'Y M', min([y_sum,m_sum]) )