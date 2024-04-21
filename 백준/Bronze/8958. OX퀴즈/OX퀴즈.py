import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    result = input().strip()
    point = 1
    total = 0
    for i in result:
        if i == 'O':
            total += point
            point += 1
        elif i == 'X':
            total += 0
            point = 1
    print(total)
            
    