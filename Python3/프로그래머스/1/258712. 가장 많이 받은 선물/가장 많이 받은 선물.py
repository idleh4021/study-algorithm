from collections import Counter

def solution(friends, gifts):
    answer = 0
    gift_score={}
    log = dict(Counter(gifts))
    get_gift_cnt ={}
    for i in friends:
        get_gift_cnt[i]=0
        gift_score[i]=0
    for i in log:
        s,r = i.split()
        gift_score[s] = log[i] if s not in gift_score else gift_score[s]+log[i]
        gift_score[r] = -log[i] if r not in gift_score else gift_score[r]-log[i]
       
        
    
    
    for f_idx in range(len(friends)):
        for r_idx in range(f_idx+1,len(friends)):
            f = friends[f_idx]
            r= friends[r_idx]
            if f==r:continue
            f_to_r = log[f'{f} {r}'] if (f'{f} {r}') in log else 0
            r_to_f = log[f'{r} {f}'] if (f'{r} {f}') in log else 0
            if f_to_r>r_to_f:
                get_gift_cnt[f] +=1
            elif f_to_r<r_to_f:
                get_gift_cnt[r] +=1
            else:
                if gift_score[f]>gift_score[r]:
                    get_gift_cnt[f] +=1
                elif gift_score[f]<gift_score[r]:
                    get_gift_cnt[r] +=1
                else : continue
            
    return max(get_gift_cnt[i] for i in get_gift_cnt)