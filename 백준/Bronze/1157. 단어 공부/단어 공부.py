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

key_max = max(alphabet_dict, key = alphabet_dict.get)
val_max = alphabet_dict.pop(max(alphabet_dict, key = alphabet_dict.get))

if val_max == alphabet_dict.pop(max(alphabet_dict, key = alphabet_dict.get)):
    print('?')
else:
    print(key_max)