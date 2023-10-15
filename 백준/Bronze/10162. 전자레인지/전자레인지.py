import sys

input = sys.stdin.readline

def solution(seconds: int):
    n = seconds
    time_list = [300, 60, 10]
    cnt_list = [0, 0, 0]

    if n % 10 != 0:
        return -1

    for i in range(3):
        cnt_list[i] = n // time_list[i]
        n -= cnt_list[i] * time_list[i]

    return cnt_list  

if __name__ == "__main__":
    seconds = int(input())
    result = solution(seconds)
    if result == -1:
        print(-1)
    else:
        print(*result)