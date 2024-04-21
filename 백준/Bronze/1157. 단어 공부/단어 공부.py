import sys
from string import ascii_uppercase

input = sys.stdin.readline
word = input().strip().upper()
alphabet_dict = {}

# 문자열 대문자 변환
for i in ascii_uppercase:
    alphabet_dict[i] = 0
    
# 알파벳 사용횟수를 기록하는 딕셔너리 생성
for i in word:
    alphabet_dict[i] += 1

# sol 2
result = [k for k,v in alphabet_dict.items() if max(alphabet_dict.values()) == v]
if len(result) == 1:
    print(result[0])
else:
    print('?')