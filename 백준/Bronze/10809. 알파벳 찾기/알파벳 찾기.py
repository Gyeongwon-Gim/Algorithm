import sys
input = sys.stdin.readline

result = [-1] * 26
S = input().strip()

for i in range(len(S)):
    if result[ord(S[i]) - 97] == -1:
        result[ord(S[i]) - 97] = i
        
print(*result)