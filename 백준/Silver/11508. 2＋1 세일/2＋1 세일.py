# 2 + 1 세일
import sys
input = sys.stdin.readline

def solution(item_list: list) -> int:
    item_list.sort(reverse = True)
    discount = 0
    for i in range(2, len(item_list), 3):
        discount += item_list[i]
    return sum(item_list) - discount

if __name__ == "__main__":
    N = int(input())
    item_list = [int(input()) for _ in range(N)]
    print(solution(item_list))