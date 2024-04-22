import sys
input = sys.stdin.readline

N = int(input())
card_list = list(map(int, input().strip().split()))
M = int(input())
search_list = list(map(int, input().strip().split()))
dict = {}
answer = []

for num in card_list:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
for num in search_list:
    if num in dict:
        answer.append(dict[num])
    else:
        answer.append(0)

print(*answer)
