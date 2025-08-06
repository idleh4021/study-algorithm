num ={'-':0,
      '\\':1,
      '(' :2,
      '@' :3,
      '?' :4,
      '>' :5,
      '&' :6,
      '%' :7,
      '/' :-1}
while True:
    s = input()
    if s == '#': break
    reverse = s[::-1]
    answer=0
    for idx, c in enumerate(reverse):
        answer += num[c] * (8 ** idx)
    print(answer)