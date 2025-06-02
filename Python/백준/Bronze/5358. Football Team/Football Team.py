import sys
while True:
    s = sys.stdin.readline().strip()
    if s == '':
        break
    a = ''.join(['i' if i=='e' else 'e' if i=='i' else 'I' if i=='E' else 'E' if i=='I' else i for i in s ])
    print(a)