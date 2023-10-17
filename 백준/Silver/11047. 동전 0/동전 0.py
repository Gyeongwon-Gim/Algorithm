# 동전 0
import sys

input = sys.stdin.readline

def solution(coin_type: list, total: int) -> int:
    count_coin = 0
    for i in reversed(range(N)):
        while (total // coin_type[i] > 0):
            total -= coin_type[i]
            count_coin += 1
    return count_coin if total == 0 else -1

if __name__ == '__main__':
    N, K = map(int, input().split())
    coin_type = [int(input()) for _ in range(N)]
    print(solution(coin_type, K))