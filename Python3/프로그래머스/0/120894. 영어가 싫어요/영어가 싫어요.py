def solution(numbers):
    num ={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
    for c in num:
        numbers =numbers.replace(c,num[c])
        
    return int(numbers)
