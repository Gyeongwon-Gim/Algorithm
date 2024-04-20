# 마지막 팩토리얼 수
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def solution(n):
    num = str(factorial(n))[::-1]
    for i in range(len(num)):
        if int(num[i]) != 0:
            print(num[i])
            break

N = int(input())
solution(N)