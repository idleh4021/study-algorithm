def solution(num_list):
    odd =num_list[0::2]
    even = num_list[1::2]
    max_val = max([sum(odd),sum(even)])
    return max_val