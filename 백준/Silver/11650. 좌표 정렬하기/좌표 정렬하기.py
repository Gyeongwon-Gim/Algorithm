import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    num_list.append([x, y])

num_list.sort()

for x, y in num_list:
    print(x, y)