# 조건: 왼쪽 괄호와 오른쪽 괄호의 개수가 같아야 한다.
# 조건2: 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다. 
def solution(string):
    stack = []
    if len(string) % 2 != 0:
        return False
    for x in string:
        if x == '(':
            stack.append(x)
        else:
            if bool(stack):
                stack.pop()          
    return True if not stack else False