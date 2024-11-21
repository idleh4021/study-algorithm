def solution(lines):
    # 선분을 나타낼 좌표를 저장할 배열 (101 크기, -100부터 100까지 사용 가능)
    line_map = [0] * 201  # -100을 0에 대응시키기 위해 200 크기로 선언

    # 각 선분의 시작과 끝을 표시
    for start, end in lines:
        for i in range(start, end):  # 구간에 해당하는 값을 증가
            line_map[i + 100] += 1  # -100에 대한 오프셋 추가

    # 두 개 이상의 선분이 겹친 부분의 길이를 계산
    overlap_length = sum(1 for count in line_map if count >= 2)
    
    return overlap_length
