# 거듭 제곱

def solution(n: int, m: int) -> int:
    if m == 1:
        return n
    return n * solution(n, m - 1)

if __name__ == "__main__":
    for _ in range(10):
        T = int(input())
        N, M = map(int, input().split())
        print(f"#{T} {solution(N ,M)}")