def solution(strArr):
    answer = []        
    return [i.lower() if index%2==0 else i.upper() for index,i in enumerate(strArr)]