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
    distances = []
    if N > 32: 
        return 0
    for case in combinations(members, 3):
        distance = 0
        for x, y in combinations(case, 2):
            distance += get_distance(x, y)
        distances.append(distance)
    return min(distances)

T = int(input())
for _ in range(T):
    print(solution())