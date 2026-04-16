
def main():
    print(solution([700, 800, 1100],[[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]],5))

def solution(schedules, timelogs, startday):
    raw_allow_schedules = list(map(lambda x: getRawTime(x)+10,schedules))
    nowday = startday

    answer = 0
    for idx ,worktimes in enumerate(timelogs):
        #sample = [worktime for addday,worktime in enumerate(worktimes) if  ((nowday+addday-1)%7 and getRawTime(worktime) > raw_allow_schedules[idx] ) < 5]
        if len([worktime for addday,worktime in enumerate(worktimes) if  ((nowday+addday-1)%7 < 5 and getRawTime(worktime) > raw_allow_schedules[idx] ) ]) ==0:
            answer +=1
        
        
    
    return answer

def getRawTime(time):
    hour,min = divmod(time , 100)
    result = (hour *60) + min
    return result

if __name__ == "__main__":
    main()