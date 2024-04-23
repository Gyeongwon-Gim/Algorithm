# 균형잡힌 세상
import sys
input = sys.stdin.readline

def solution(string):
    stack = []
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ')':
            if stack:
                if stack.pop() == '(':
                    continue
                else:
                    return 'no'
            else:
                return 'no'
        elif i == ']':
            if stack:
                if stack.pop() == '[':
                    continue
                else:
                    return 'no'
            else:
                return 'no'            
    if not stack: 
        return 'yes'   
    return 'no'

while True:
    string = input().rstrip()
    if string == '.':
        break
    print(solution(string))