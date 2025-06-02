_from = int(input())
_to = int(input())

for i in range(_from,_to+1):
    if(i== _from):
        print(f'All positions change in year {_from}')
        continue
    gap  = abs(_from - i)
    if gap%4 ==0 and gap%3==0 and gap%5==0:
        print(f'All positions change in year {i}')