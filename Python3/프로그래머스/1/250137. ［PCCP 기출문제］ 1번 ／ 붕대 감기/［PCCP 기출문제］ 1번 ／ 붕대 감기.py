def solution(bandage, health, attacks):
    answer = 0
    max_health = health
    heal_time = bandage[0]
    heal_per_sec = bandage[1]
    heal_bonus = bandage[2]
    heal_stack = 0
    attacks = sorted(attacks,reverse=True)
    wait_attack =[]
    for i in range(attacks[0][0]):
        if len(wait_attack)==0: wait_attack=attacks.pop()
        sec = i+1
        if wait_attack[0] == sec:
            health-=wait_attack[1]
            if health<=0 : return -1
            heal_stack=0
            wait_attack= []
            continue
        heal_stack+=1
        health += heal_per_sec
        if health>max_health: health= max_health
        if heal_stack==heal_time:
            health+=heal_bonus
            if health>max_health: health= max_health
            heal_stack =0
            
        
        
    
    return health