a,b,v = input().split()

a,b,v = int(a),int(b),int(v)
answer = 0
days_climb = a-b

answer = (v-a)//days_climb +1
rest = (v-a)%days_climb
if rest >0 : answer+=1

print(answer)
