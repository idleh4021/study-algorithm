def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        arr=[]
        for j in range(n):
            arr.append(num_list[j+n*i])
        answer.append(arr)
    return answer
