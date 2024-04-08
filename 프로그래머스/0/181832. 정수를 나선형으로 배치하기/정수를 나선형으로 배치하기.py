def solution(n):
    result = [[0 for i in range(n)] for j in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]    
    x, y = 0, 0
    value = 1
    direction = 0
    
    while value <= n*n:
        result[x][y] = value
        value += 1
        x = x + dx[direction]
        y = y + dy[direction]
        
        # 뱡향 전환을 해야 하는 경우
        # 1. 인덱스가 리스트의 범위를 벗어난 경우 
        # 2. 인덱스가 범위를 벗어나지 않았지만 값이 입력된 경우 
        if x >= 0 and y >= 0 and x < n and y < n and result[x][y] == 0:
            continue
        else:
            # 덧셈 취소
            x = x - dx[direction]
            y = y - dy[direction]
            # 방향 전환
            direction = (direction + 1) % 4
            # 위치 업데이트
            x = x + dx[direction]
            y = y + dy[direction]
        
    return result

