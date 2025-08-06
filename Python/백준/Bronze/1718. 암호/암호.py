alpabet = list('abcdefghijklmnopqrstuvwxyz')

t= input()
k = input()

def encrypt(text, key):
    result =''
    for i,c in enumerate(text):
        if ord(c) == 32:
            result += c
        else:
            num = ord(c) - ord(key[i % len(key)]) -1
            result += alpabet[num]
    return result

print(encrypt(t, k))