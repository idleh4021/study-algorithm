def solution(intStrs, k, s, l):
    return [int(i[s:s+l]) for i in intStrs if int(''.join(i[s:s+l]))>k]