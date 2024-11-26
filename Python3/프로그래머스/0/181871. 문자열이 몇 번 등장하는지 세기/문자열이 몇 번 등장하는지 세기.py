def solution(myString, pat):
    cnt =0
    for idx , c in enumerate(myString):
        if(myString[idx:len(pat)+idx]==pat):cnt+=1
    return cnt