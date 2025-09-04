R,C = map(int,input().split())
A,B = map(int,input().split())
last_c = 'X'
for r in range(R):
    s =''
    for c in range(C):
        s += last_c*B
       
        last_c = 'X' if last_c=='.' else '.'
    for a in range(A):
        print(s)
    if C%2 ==0:  last_c = 'X' if last_c=='.' else '.'
    
        
        
    