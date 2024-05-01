import sys
from itertools import combinations
input = sys.stdin.readline

def get_distance(x, y):
    score = 0
    if x[0][0] != y[0][0]:
        score += 1
    if x[0][1] != y[0][1]:
        score += 1
    if x[0][2] != y[0][2]:
        score += 1
    if x[0][3] != y[0][3]:
        score += 1
    return score

def solution():
    N = int(input())
    id = [i for i in range(N)]
    members = list(zip(input().rstrip().split(), id))
    distance = []
    if N > 32: 
        return 0
    for a, b, c in combinations(members, 3):
        dist = 0
        dist += get_distance(a, b)
        dist += get_distance(b, c)
        dist += get_distance(a, c)
        distance.append(dist)
    return min(distance)

T = int(input())
for _ in range(T):
    print(solution())