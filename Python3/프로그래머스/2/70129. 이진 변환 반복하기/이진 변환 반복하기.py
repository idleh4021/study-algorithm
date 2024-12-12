def solution(s):
    bin_cnt,zero_cnt = 0,0
    while(len(s)!=1):
        zero_cnt += s.count('0')
        s = s.replace('0','')
        s =str(bin(int(len(s))))
        s= s.replace('0b','')
        bin_cnt+=1
    return [bin_cnt,zero_cnt]
