import sys
input = sys.stdin.readline

M = int(input())
num_set = set()
for _ in range(M):
    order = input().split()
    if order[0] == 'add':
        num_set.add(int(order[1]))
    elif order[0] == 'remove':
        num_set.discard(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in num_set:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in num_set:
            num_set.remove(int(order[1]))
        else:
            num_set.add(int(order[1]))
    elif order[0] == 'all':
        num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif order[0] == 'empty':
        num_set.clear()
