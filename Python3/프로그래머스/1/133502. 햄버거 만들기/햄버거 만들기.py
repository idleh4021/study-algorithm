def solution(ingredient):
    answer = 0
    ingredient =list(reversed(ingredient))
    stacks=''
    while len(ingredient)>0:
        stacks+= str(ingredient.pop())
        if stacks[-4:] =='1231':
        #temp = stacks.replace('1231','')
            stacks = stacks[:-4]
            answer+=1
            #answer += (len(stacks)-len(temp))//4
            #stacks = temp       
    
    return answer