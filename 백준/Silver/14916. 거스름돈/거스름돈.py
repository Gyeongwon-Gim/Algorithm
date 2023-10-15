# 거스름돈
import sys

def solution(n: int) -> int:
    if n == 1 or n == 3:
        return -1
    return even_num(n) if n % 2 == 0 else odd_num(n)
    
def even_num(n: int) -> int:
    return operation(n)

def odd_num(n: int) -> int:
    n -= 5
    return operation(n) + 1 
 

def operation(num: int) -> int:
    coin_two = (num % 10) // 2
    result = coin_two
    num -= coin_two * 2
    
    coin_five = num // 5
    result += coin_five
    return result

input = sys.stdin.readline
n = int(input())
print(solution(n))
