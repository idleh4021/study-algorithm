def solution(myStr):
    answer= myStr.replace('a','c').replace('b','c').split('c')
    return [i for i in answer if i !=''] if len([i for i in answer if i !='']) != 0 else ['EMPTY']