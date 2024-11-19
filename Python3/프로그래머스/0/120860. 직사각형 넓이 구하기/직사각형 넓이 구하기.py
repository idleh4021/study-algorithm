def solution(dots):
    answer = 0
    x_p1 = dots[0][0]
    y_p1 = dots[0][1]
    x_len = 0
    y_len = 0
    for index,pts in enumerate(dots):
        if index==0: continue
        if(y_p1==pts[1]):x_len = abs( pts[0] - x_p1)
        if(x_p1==pts[0]):y_len = abs(pts[1]-y_p1)
        if(x_len !=0 and y_len !=0): return x_len*y_len
    return answer