def solution(wallpaper):
    answer = []
    lux,luy =999,999
    rdx,rdy = 0,0
    
    for i in range(len(wallpaper)):
        if('#' in wallpaper[i]):
            if lux>i : lux = i
            if rdx<i  : rdx = i
            arr = [idx for idx,j in enumerate(wallpaper[i]) if j =='#']
            min_y = min(arr)
            max_y = max(arr)
            if luy>min_y : luy = min_y
            if rdy<max_y : rdy = max_y
            
    return [lux,luy,rdx+1,rdy+1]