def solution(myString, pat):
    return int(pat in myString.replace('A','9').replace('B','A').replace('9','B'))