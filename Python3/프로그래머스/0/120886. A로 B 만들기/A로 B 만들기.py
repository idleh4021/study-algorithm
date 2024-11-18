def solution(before, after):
    list_after = list(after)
    for i in before:
        if(i in list_after):
            list_after.remove(i)
    return 1 if len(list_after)==0 else 0