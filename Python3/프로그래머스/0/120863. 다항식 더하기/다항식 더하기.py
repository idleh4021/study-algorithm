def solution(polynomial):
    split_list = polynomial.split(' ')
    x_list = [i for i in split_list if 'x' in i]
    num_list =[int(i) for i in split_list if 'x' not in i and '+' not in i]
    x_count = sum( int(i.replace('x','1' if len(i)==1 else '')) for i in x_list )
    
    return (str(x_count) if x_count>1 else '') +('x' if x_count>0 else '')+((' + ' if x_count>0 else '')+str(sum(num_list)) if sum(num_list) !=0 else '' )
