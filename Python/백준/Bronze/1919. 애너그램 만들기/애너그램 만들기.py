def SetAlphabetDict():
    result = {}
    for i in range(26):
        result[chr(i+97)] = 0
    return result

def GetCntOfAlphabet(dict,s):
    for c in s:
        dict[c]+=1

a_str =SetAlphabetDict()
b_str =SetAlphabetDict()
GetCntOfAlphabet(a_str,input())
GetCntOfAlphabet(b_str,input())

cnt = 0
for i in a_str:
    cnt += abs(a_str[i] -b_str[i])
print(cnt)

