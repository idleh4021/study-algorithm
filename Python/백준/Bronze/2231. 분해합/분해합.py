def sum_of_digits(n):        
    return sum(list(map(int,list(str(n)))))
n= input()
answer = 0
for i in range(1, int(n)+1):
    if(i+sum_of_digits(i) == int(n)):
        answer = i
        break
print(answer)
