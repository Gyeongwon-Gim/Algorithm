import sys
from collections import deque
input = sys.stdin.readline

def solution(priorities, location):
     cnt = 0
     pointer = location
     priorities = deque(priorities)
    
     while priorities:
         x = priorities.popleft()
         cnt += 1
         pointer -= 1
         for y in priorities:
             if y > x:
                 priorities.append(x)
                 cnt -= 1
                 # 예외
                 if pointer == -1:
                     pointer = len(priorities) -1
                 break
        
         if pointer == -1:
             return cnt
TC = int(input())

for _ in range(TC):
    N, M = map(int, input().split())
    priorities = list(map(int, input().strip().split()))
    print(solution(priorities, M))
    