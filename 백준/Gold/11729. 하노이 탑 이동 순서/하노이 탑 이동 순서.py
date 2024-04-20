def solution(n):
    answer = []
    def hanoi_tower(n, A, B, C):
        if n == 1:
            answer.append([A, C])
        else:
            hanoi_tower(n-1, A, C, B)
            answer.append([A, C])
            hanoi_tower(n-1, B, A, C)
        return answer
    
    return hanoi_tower(n, 1, 2, 3)

N = int(input())
result = solution(N)
print(len(result))
for a, b in result:
    print(a, b)
