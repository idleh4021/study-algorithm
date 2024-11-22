def solution(num_list):
    odd =num_list[0::2]
    even = num_list[1::2]
    return sum(odd) if sum(odd)>sum(even) else sum(even)