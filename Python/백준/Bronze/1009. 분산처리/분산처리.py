import sys
dic={0:[0],1:[1],2:[2,4,8,6],3:[3,9,7,1],4:[4,6],5:[5],6:[6],7:[7,9,3,1],8:[8,4,2,6],9:[9,1]}


for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    t_n = a%10
    arr = dic[t_n]
    idx = b%len(arr)
    if idx ==0 : idx = -1
    else : idx -= 1
    answer = arr[idx]
    print(answer if answer != 0 else 10)
    #print(dic[a%10][b%(len(dic[a%10]))-(1 if ])
