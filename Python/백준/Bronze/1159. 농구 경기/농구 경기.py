players = {}
answer = ""
for i in range(int(input())):
    name = input()
    c = name[0]
    if c in players:
        players[c] += 1
    else:
        players[c] = 1
for player in players:
    if players[player] >= 5:
        answer+= player
print('PREDAJA' if answer == "" else ''.join(sorted(answer)))
