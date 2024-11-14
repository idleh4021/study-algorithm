str= input()
for c in str:
    print( c.upper() if c.islower() else c.lower(),end='')