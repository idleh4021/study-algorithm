def solution(myStr):
    #split 매개변수 없이 처리
    answer= myStr.replace('a',' ').replace('b',' ').replace('c',' ').split()
    return answer if len(answer)>0 else ['EMPTY']
    #기존답
    #answer= myStr.replace('a','c').replace('b','c').split('c')
    #return [i for i in answer if i !=''] if len([i for i in answer if i !='']) != 0 else ['EMPTY']