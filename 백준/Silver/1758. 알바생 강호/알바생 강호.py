import sys

def solution(n: int) -> int:
    tip_list = []
    num_list = [i for i in range(n)]
    for _ in range(n):
        tip_list.append(int(input()))
    tip_list.sort(reverse = True)
    tip_list = list(map(lambda x, y: x - y, tip_list, num_list))
    
    return sum(filter(lambda x: x > -1, tip_list))

input = sys.stdin.readline
N = int(input())
print(solution(N))