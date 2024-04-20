def hanoi_tower(n, from_, temp, to):
    if n == 1:
        print(from_, to)
    else:
        hanoi_tower(n-1, from_, to, temp)
        print(from_, to)
        hanoi_tower(n-1, temp, from_, to)

N = int(input())
print(2 ** N - 1)
if N <= 20:
    hanoi_tower(N, 1, 2, 3)


