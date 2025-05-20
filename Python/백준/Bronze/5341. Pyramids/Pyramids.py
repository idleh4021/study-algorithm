while(True):
    layer = int(input())
    if(layer==0): break
    print((1+layer)*(layer//2)+(0 if layer %2 ==0 else (layer//2+1)) )
    
        