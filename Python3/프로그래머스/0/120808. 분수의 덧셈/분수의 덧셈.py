def solution(numer1, denom1, numer2, denom2):
    numer1_b = numer1 * denom2
    denom1_b = denom1 * denom2
    numer2_b = numer2 * denom1
    
    totalnumer = numer1_b+numer2_b
    totaldenom = denom1_b
    list_devide_num = []
    for i in range(2 ,(denom1 if denom1<denom2 else denom2)+1) :
        while(totaldenom % i==0 and totalnumer % i ==0):
            totalnumer=int(totalnumer/i)
            totaldenom=int(totaldenom/i)
    
 #  if(int(totalnumer / denom1) >0 and  totalnumer % denom1 ==0):
 #      totalnumer /= denom1
 #      totaldenom /= denom1
 #  
 #  if(int(totalnumer / denom2) >0 and totalnumer % denom2 ==0):
 #      totalnumer /= denom2
 #      totaldenom /= denom2
    
    answer = [int(totalnumer),int(totaldenom)]
    return answer