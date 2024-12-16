def solution(n, words):
    answer = []
    say_list = []
    for idx,word in enumerate(words):
        if idx !=0 and word[0] != words[idx-1][-1]:
            return [ (idx+1)%n if (idx+1)%n != 0 else n , ((idx+1)//n)+(1 if (idx+1)%n != 0 else 0 )]
        elif word not in say_list:
            say_list.append(word)
            continue
        else :return [(idx+1)%n if (idx+1)%n != 0 else n , ((idx+1)//n)+(1 if (idx+1)%n != 0 else 0 )]
    return [0,0]
