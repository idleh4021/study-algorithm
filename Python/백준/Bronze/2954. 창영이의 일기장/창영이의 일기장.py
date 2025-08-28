s = input()
arr=['a','e','i','o','u']
suffix = 'p'
for i in arr:
    s = s.replace(i+suffix+i,i)
print(s)