
r_tile, b_tile = map(int,input().split())
tiles = sum([r_tile,b_tile])

for i in range(int(tiles**0.5),0,-1):
    if tiles % i == 0:
        L,W = tiles // i , i
        if (L-2)*(W-2) == b_tile:
            print(L,W)
            break
