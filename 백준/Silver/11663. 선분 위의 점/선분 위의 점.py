# 선분 위의 점
import sys
input = sys.stdin.readline

def binary_search(target, num_list):
    left = 0
    right = len(num_list) - 1
    while left < right:
        mid = (left + right) // 2
        if num_list[mid] == target:
            return mid
        elif num_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
    
N, M = map(int, input().split())
dots = sorted(map(int, input().split()))
dots.sort()

for _ in range(M):
    start, end = map(int, input().split())
    result = binary_search(start, dots)
    start_idx = result if dots[result] >= start else result + 1
    result = binary_search(end, dots)
    end_idx = result if dots[result] <= end else result - 1
    print(end_idx - start_idx + 1)
