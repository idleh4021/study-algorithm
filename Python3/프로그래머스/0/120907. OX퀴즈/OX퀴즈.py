def solution(quizs):
    answer=[]
    for quiz in quizs:
        array_1 = quiz.split(' ')
        result = array_1[array_1.index('=')+1]
        calc_result=0
        calc ='+'
        for index,val in enumerate(array_1):
            
            if val =='=': break
            if index%2==0:
                calc_result += int(val) if calc=='+' else -int(val)
            else: calc =val
        answer+='O' if int(result)==int(calc_result) else 'X'

    return answer

        