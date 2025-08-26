ban = 'CAMBRIDGE'

s = input()
print(*list(map(lambda x : '' if x in ban else x , s)),sep='')
