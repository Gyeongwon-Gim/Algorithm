A = int(input())
B = int(input())
C = int(input())

cnt_list = [0] * 10
result = str(A * B * C)
for i in range(len(result)):
    cnt_list[int(result[i])] += 1

for i in range(10):
    print(cnt_list[i])