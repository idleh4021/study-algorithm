def solution(n):
    answer = 0
    i = n+1
    while(True):
        bin_n_cnt = str(bin(n)).replace('0b','').count('1')
        bin_i_cnt = str(bin(i)).replace('0b','').count('1')
        if(bin_n_cnt == bin_i_cnt): break
        i+=1
    return i