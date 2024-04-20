TC = int(input())
for i in range(TC):
    N, string = input().split()
    N = int(N)
    answer = ''
    # print(string * int(N))
    for i in string:
        answer += i * N
    print(answer) 