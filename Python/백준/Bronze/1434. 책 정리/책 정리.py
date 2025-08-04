N,M = map(int, input().split()) #N 박스의 개수 M 책의 개수
boxes = list(map(int, input().split())) #박스의 크기
books = list(map(int, input().split())) #책의 크기
answer =0 

box =book = 0
while len(books) > 0 or book > 0:
    if box ==0:
        box = boxes.pop(0) #박스 하나를 꺼냄
    if book ==0:
        book = books.pop(0) #책 하나를 꺼냄
    if box > book:
        box -= book #박스에서 책의 크기만큼 줄임
        book = 0
    elif box == book:
        box= book = 0
    else:
        answer += box
        box = 0
print(answer+box+sum(boxes))
