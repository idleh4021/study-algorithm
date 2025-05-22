card_qty,target = map(int, input().split())
cards = list(map(int, input().split()))
cards = sorted(cards)
answer =0
while len(cards) > 3:
    a= cards.pop()
    for idx,b in enumerate(cards):
        for c in cards[idx+1:]:
            sum_val = a+b+c
            if(sum_val > target):
                break
            elif(sum_val == target):
                answer=sum_val
                break
            else:
                if(abs(target-sum_val) < abs(target-answer)):
                    answer = sum_val
        if (answer == target):
            break
    if (answer == target):
        break
print(answer)
            
        