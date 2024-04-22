import sys
input = sys.stdin.readline

N = int(input())
def solution(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        if i == ')':
            if stack:
                stack.pop()
            else:
                return 'NO'
    if not stack:
        return 'YES'    
    return 'NO'

for _ in range(N):
    ps = input().strip()
    print(solution(ps))