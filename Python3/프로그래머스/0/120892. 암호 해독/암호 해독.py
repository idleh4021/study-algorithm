def solution(cipher, code):
    cnt = len(cipher)//code
    answer =''
    for i in range(1,cnt+1):
        answer +=cipher[(i*code)-1]

    return answer