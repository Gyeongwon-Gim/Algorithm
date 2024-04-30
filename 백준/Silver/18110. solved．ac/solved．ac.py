# solved.ac
import sys
from collections import deque
input = sys.stdin.readline

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)
    
N = int(input())
difficulty_list = []

for _ in range(N):
    difficulty_list.append(int(input()))

difficulty_list.sort()
difficulty_list = deque(difficulty_list)
slice_num = my_round(N*0.15)

for _ in range(slice_num):
    if len(difficulty_list) != 0:
        difficulty_list.popleft()
    if len(difficulty_list) != 0:
        difficulty_list.pop()
# print(f'slice_num: {slice_num}, difficulty_list: {difficulty_list}')       
# 인덱스 슬라이싱
# difficulty_list = difficulty_list[slice_num:]
# difficulty_list = difficulty_list[:-slice_num]


if difficulty_list:
    result = my_round(sum(difficulty_list)/len(difficulty_list))
    print(result)
else:
    print(0)