def solution(keymap, targets):
    answer = []
    keys_cnt ={}
    keymap_word = set(''.join(keymap))
    for k in keymap_word:
        #keys_cnt[k] =min([i%len(keymap[0])+1 for i,v in enumerate(''.join(keymap)) if k==v ])
        keys_cnt[k] = -1
        for line in keymap:
            if k in line:
                idx = list(line).index(k)
                if keys_cnt[k] ==-1 or keys_cnt[k]>idx:
                    keys_cnt[k]=idx+1
                if idx+1 == 1:break
                
            
    
    for target in targets:
        try:
            ans = sum([keys_cnt[c] for c in target])
            answer.append(ans)
        except:
            answer.append(-1)
    return answer

