def solution(n):
    six = 6
    val = 1
    if n % 2 ==0:
        six =six // 2
        n = n//2
        val *=2
    if n % 3==0:
        six = six //3
        n = n//3
        val*=3
    return n*six*val//6