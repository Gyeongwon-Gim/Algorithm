# 숫자를 정렬하자
if __name__ == "__main__":
    TC = int(input())
    for tc in range(1, TC + 1):
        num_list = []
        N = int(input())
        num_list = list(map(int, input().split()))
        num_list.sort()
        print(f"#{tc}", end=" ")
        print(*num_list)
