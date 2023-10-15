# 거스름돈
import sys

def solution(n: int) -> int:
    if n == 1 or n == 3:
        return -1
    answer = 0
    if n % 2 == 0:
        answer = even_number(n)
    else:
        answer = odd_number(n)
    return answer
    
def even_number(n: int) -> int:
    result = 0
    
    coin_two = (n % 10) // 2
    result += coin_two
    n -= coin_two * 2

    coin_five = n // 5
    result += coin_five

    return result

def odd_number(n: int) -> int:
    n -= 5
    result = 1 

    coin_two = (n % 10) // 2
    result += coin_two
    n -= coin_two * 2
    
    coin_five = n // 5
    result += coin_five
    
    return result


input = sys.stdin.readline
n = int(input())
print(solution(n))
