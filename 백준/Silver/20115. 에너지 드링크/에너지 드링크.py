import sys

input = sys.stdin.readline

def solution(drink_list: list) -> float:
    for i in range(N-1):
        drink_list[-1] += drink_list[i] / 2
    return drink_list[-1]

if __name__ == "__main__":
    N = int(input())
    drink_list = list(map(int, input().split()))
    drink_list.sort()
    print(solution(drink_list))