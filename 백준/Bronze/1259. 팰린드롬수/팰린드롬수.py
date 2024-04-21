import sys
input = sys.stdin.readline

def solution(string):
    string_reverse = string[::-1]
    for i in range(len(string)):
        if string[i] != string_reverse[i]:
            return 'no'
    else:
        return 'yes'

string = input().strip()
while string != '0':
    print(solution(string))
    string = input().strip()