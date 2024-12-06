def solution(t, p):
    list_t = [t[i:i+len(p)] for i in range(len(t)-len(p)+1)]
    return len([i for i in list_t if i<= p])