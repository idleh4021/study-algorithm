a=input()
arr = list(map(int, input().split()))
sort_arr = sorted(arr)
answer = [arr.index(i)+2 for i in sort_arr]
print(f'1 {" ".join(map(str,answer))}')
#print([idx+2 for idx,i in enumerate(arr) ])

