def solution(s, skip, index):
    answer = ''
    for c in s:
        st_idx= ord(c)-ord('a')
        #ed_idx= ord(c)+index-ord('a')
        left_move = index
        while left_move!= 0 :
            st_idx+=1
            if getAlphabet(st_idx) in skip:
                continue
            left_move-=1
        answer+=getAlphabet(st_idx)

        
        
        
    return answer

def getAlphabet(num):
    return chr(num%26+ord('a'))