def solution(bin1, bin2):
    answer = int(f'0b{bin1}',2) + int(f'0b{bin2}',2)
    return str(bin(answer)).replace('0b','')