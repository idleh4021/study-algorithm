a = '9780921418'
for _ in range(3):
    a+=input()

sum = sum([ int(i) *(1 if (idx+1) %2 == 1 else 3) for idx, i in enumerate(a)])
print('The 1-3-sum is',sum)