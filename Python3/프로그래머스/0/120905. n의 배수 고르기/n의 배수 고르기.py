def solution(n, numlist):
    for num in reversed(numlist):
        if(num%n!=0) : numlist.remove(num)
    return numlist