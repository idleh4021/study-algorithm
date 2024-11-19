def solution(spell, dic):
    spell_sorted = sorted(spell)
    for word in dic:
        dic_sorted=sorted(list(word))
        if(spell_sorted == dic_sorted): return 1
    return 2
