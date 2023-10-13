# 10162 전자레인지
import sys

input = sys.stdin.readline

T = int(input())

coin_list = [25, 10, 5, 1]
cnt_list = [0, 0, 0, 0]
# quarter, dime, nickel, penny = coin_list[0], coin_list[1], coin_list[2], coin_list[3]

# for _ in range(T):
#     n = int(input())
    
#     cnt_list[0] = n // quarter
#     n -= cnt_list[0] * quarter

#     cnt_list[1] = n // dime
#     n -= cnt_list[1] * dime

#     cnt_list[2] = n // quarter
#     n -= cnt_list[2] * nickel

#     cnt_list[3] = n

#     print(*cnt_list)

for _ in range(T):
    n = int(input())
    for i in range(4):
        cnt_list[i] = n // coin_list[i]
        n -= cnt_list[i]*coin_list[i]
    print(*cnt_list)