import sys
input = sys.stdin.readline

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
num_list = list(map(int, input().strip().split()))
cnt = 0

for i in range(N):
    if is_prime(num_list[i]):
        cnt += 1
print(cnt)
    