a =int(input())
b =int(input())
c =int(input())
sum_val =sum([a,b,c])
answer =''
if sum_val != 180  : answer ='Error'
elif a==b and b==c and a==60: answer = 'Equilateral'
elif a!=b and b!=c and a!=c : answer = 'Scalene'
else : answer = 'Isosceles'
print(answer)