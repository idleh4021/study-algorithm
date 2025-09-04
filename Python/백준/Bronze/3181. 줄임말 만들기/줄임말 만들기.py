exclude_word =['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
words = input().split()
f = words.pop(0)
arr = filter(lambda x: x not in exclude_word,words)
s = f[0].upper() + ''.join([i[0].upper() for i in arr])
print(s)


