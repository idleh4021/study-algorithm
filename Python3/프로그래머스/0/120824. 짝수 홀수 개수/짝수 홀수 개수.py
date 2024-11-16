def solution(num_list):
    even_cnt =len([i for i in num_list if i%2==0])
    odd_cnt = len([i for i in num_list if i%2!=0])
    answer = [even_cnt,odd_cnt]
    
    return answer