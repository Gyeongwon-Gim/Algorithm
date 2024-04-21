# 나이순 정렬
import sys
input = sys.stdin.readline

N = int(input())
order = 0
member_list = []
for _ in range(N):
    age, name = input().split()
    member_list.append([age, name, order])
    order += 1
member_list.sort(key = lambda x : (int(x[0]), x[2]))

for a, g, odr in member_list:
    print(a, g)