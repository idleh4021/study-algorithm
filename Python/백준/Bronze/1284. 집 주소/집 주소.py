import sys
width ={1:2,0:4}
while True:
    i = sys.stdin.readline().strip('\n')
    if(i=='0'): break
    gap = len(i)+1
    widths = [3 if int(j) not in width else width[int(j)] for j in str(i)]
    print(sum(widths)+gap)
