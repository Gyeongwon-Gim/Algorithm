import sys
input = sys.stdin.readline

def solution(person_list: int)-> int:
    person_list.sort()
    for i in range(len(person_list)):
        if i == 0: continue
        person_list[i] += person_list[i-1]
    return sum(person_list)
 
if __name__ == "__main__":
    N = int(input())
    person_list = list(map(int, input().split()))
    print(solution(person_list))