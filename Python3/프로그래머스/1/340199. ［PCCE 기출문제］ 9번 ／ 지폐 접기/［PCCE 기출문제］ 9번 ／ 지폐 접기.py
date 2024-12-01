def solution(wallet, bill):
    
    answer = bill
    cnt=0
    while not bill_in_pocket(wallet,answer):
        answer=fold(answer)
        cnt+=1
        
    return cnt

def bill_in_pocket(wallet,bill):
    sort_wallet = sorted(wallet)
    sort_bill = sorted(bill)
    return True if sort_wallet[0] >= sort_bill[0] and sort_wallet[1] >= sort_bill[1] else False

def fold(bill):
    sort_bill = sorted(bill)
    sort_bill[1] = sort_bill[1]//2
    return sort_bill
        
        