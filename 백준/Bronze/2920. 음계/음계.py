import sys
input = sys.stdin.readline
num_list = list(map(int, input().split()))
def check_asc(num_list):
    answer_list = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(8):
        if num_list[i] == answer_list[i]:
            continue
        else: return 'mixed'
    return 'ascending'
    
def check_des(num_list):
    answer_list = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(8):
        if num_list[i] == answer_list[i]:
            continue
        else:
            return 'mixed'
    return 'descending'

if num_list[0] == 1:
    print(check_asc(num_list))
elif num_list[0] == 8:
    print(check_des(num_list))
else:
    print('mixed')
