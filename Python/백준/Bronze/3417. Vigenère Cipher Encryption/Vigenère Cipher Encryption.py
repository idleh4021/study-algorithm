def crypt(key,value):
    asc = ord(key)+ord(value)
    return chr((asc+1)%26 +65)

while True:
    key = input()
    if key =='0' : break
    values = input()
    answer =''
    for i,v in enumerate(values):
        answer += crypt(key[i%len(key)],v)
    print(answer)
    