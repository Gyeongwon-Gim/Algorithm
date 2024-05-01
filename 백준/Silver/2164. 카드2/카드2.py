import sys
from collections import deque
input = sys.stdin.readline

def solution(num_list):
    num_list = deque(num_list)
    while len(num_list) > 1:
        # 맨 위의 카드 버리기
        num_list.popleft()
        # 카드 맨 뒤로 보내기
        if len(num_list) == 1:
            break
        else:
            card = num_list.popleft()
            num_list.append(card)
    return num_list[-1] 
        
N = int(input())
num_list = [i for i in range(1, N + 1)]
print(solution(num_list))
