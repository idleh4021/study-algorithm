N,M,L = map(int, input().split()) # N : 사람 수 , M : 게임오버 카운터 , L : 공을 던지는 간격
cnt_balls = {}
cnt_balls[0] = 1 # 1번사람이 공을가지고 시작
holdplayer = 0
answer = 0
while(True):
    if cnt_balls.get(holdplayer,-1) == M: # holdplayer가 M개를 가지면 게임오버
        print(answer)
        break
    if cnt_balls.get(holdplayer,0) % 2 == 1 : # 홀수면 시계방향으로 L 번째사람
        holdplayer = (holdplayer + L ) % N
    else:
        holdplayer = holdplayer - L
        if holdplayer < 0: # 0번사람은 존재하지 않으므로 1번사람으로
            holdplayer = holdplayer + N
    cnt_balls[holdplayer] = cnt_balls.get(holdplayer, 0) + 1 # holdplayer가 리스트에 없으면 default값 0 
    answer +=1

        




