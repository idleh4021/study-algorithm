while True:
    a,b = input().split()
    a,b = int(a),int(b)
    if a==b and b==0:    break
    if b%a ==0 :print('factor')
    elif a%b ==0 : print('multiple')
    else : print('neither')
    