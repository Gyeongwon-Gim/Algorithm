# board: 게임 화면의 격자의 상태가 담긴 2차원 배열
# moves: 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return
def solution(board, moves):
    answer = 0
    stack = []
    moves = [(i-1) for i in moves]
    for loc in moves:
        for i in range(len(board)):
            if board[i][loc] != 0:
                stack.append(board[i][loc])
                board[i][loc] = 0
                if (len(stack) >= 2) and(stack[-1] == stack[-2]):
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer