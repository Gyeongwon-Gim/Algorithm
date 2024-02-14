from collections import deque

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    # brown + yellow를 두 개의 약수로 인수분해 한 경우의 수 m * n 에 대하여
    # (m-2)*(n-2) == yellow -> True 인 경우를 찾는다.
    for i in range(1, int(total**(1/2)) + 1):
        if (total % i) == 0:
            j = total / i
        if (i - 2)*(j - 2) == yellow:
            return [i, j] if i > j else [j, i]
        