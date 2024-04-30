# 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 듣도 못한 사람
never_heard = set()
# 보도 못한 사람
never_seen = set()
for _ in range(N):
    never_heard.add(input().rstrip())
for _ in range(M):
    never_seen.add(input().rstrip())

answer = list(never_seen & never_heard)
answer.sort()
print(len(answer))
for i in answer:
    print(i)