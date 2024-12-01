def solution(video_len, pos, op_start, op_end, commands):
    answer = skipOp(pos,op_start,op_end)
    for c in commands:
        
        if c=='prev':
            answer = prevCommand(video_len,answer)
        elif c=='next':
            answer = nextCommand(video_len,answer)
        else : 
            skipOp(answer,op_start,op_end)
        answer = skipOp(answer,op_start,op_end)
    return answer

def nextCommand(video_len,pos):
    video_sec = convertToSecond(video_len)
    pos_sec = convertToSecond(pos)
    if pos_sec+10>= video_sec:
        return convertToTime(video_sec)
    else : return convertToTime(pos_sec +10 )

def prevCommand(video_len,pos):
    video_sec = convertToSecond(video_len)
    pos_sec = convertToSecond(pos)
    if pos_sec-10<0:
        return "00:00"
    else : return convertToTime(pos_sec -10 )

def skipOp(pos,op_start,op_end):
    pos_sec = convertToSecond(pos)
    op_st_sec = convertToSecond(op_start)
    op_ed_sec = convertToSecond(op_end)
    if op_st_sec <= pos_sec and pos_sec <= op_ed_sec:
        return op_end
    else :return pos
    
def convertToSecond(time):
    arr = time.split(":")
    answer = int(arr[1])
    answer += int(arr[0])*60
    return answer
    
def convertToTime(seconds):
    return str(f'{int(seconds)//60:02d}')+":"+str(f'{int(seconds)%60:02d}')




