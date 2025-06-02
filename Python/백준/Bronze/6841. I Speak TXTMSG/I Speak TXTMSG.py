import sys

emoge ={'CU':	'see you'
        ,':-)':	'I’m happy'
        ,':-(':	'I’m unhappy'
        ,';-)':	'wink'
        ,':-P':	'stick out my tongue'
        ,'(~.~)':	'sleepy'
        ,'TA':	'totally awesome'
        ,'CCC':	'Canadian Computing Competition'
        ,'CUZ':	'because'
        ,'TY':	'thank-you'
        ,'YW':	'you’re welcome'
        ,'TTYL':	'talk to you later'}

while True:
    msg = sys.stdin.readline().strip()
    if msg =='':
        break
    print(emoge[msg] if msg in emoge else msg)  
