# 수 찾기
import sys
input = sys.stdin.readline
def binary_search(num, num_list):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2 
        if num > num_list[mid]:
            start = mid + 1
        elif num < num_list[mid]:
            end = mid - 1
        else:
            return 1
    else: 
        return 0
    
def solution(A, B):
    result = []
    for element in B:
        result.append(binary_search(element, A))
    return result   
             
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))
answer = solution(A, B)
print(*answer)