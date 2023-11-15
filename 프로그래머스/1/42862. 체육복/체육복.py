# def solution(n, lost, reserve):
#     # 전체 학생의 번호를 담을 리스트 선언
#     total = set()
#     lost = set(lost)
    
#     for i in range(1, n+1):
#         total.add(i)
#     print(total)
    
#     reserve1 = reserve.copy()
#     reserve2 = reserve.copy()
    
#     for i in range(len(reserve)):
#         reserve1.append(reserve[i]+1)
        
#     for i in range(len(reserve)):
#         reserve2.append(reserve[i]-1)
    
#     reserve1 = set(reserve1)
#     reserve2 = set(reserve2)
        
#     no_wear1 = lost - reserve1
#     no_wear2 = lost - reserve2
    
#     print(reserve1, reserve2, sep=' %% ')
    
#     answer1 = total - no_wear1
#     answer2 = total - no_wear2
#     print(answer1, answer2, sep=' - ')
#     # return len(answer1) if len(answer1) >= len(answer2) else len(answer2)
#     return len(answer1)

def solution(n: int, lost: list, reserve: list) -> int:
    student = [1] * n
    max_count = 0
    lost.sort()
    reserve.sort()
    for num in lost:
        student[num - 1] -= 1
    for num in reserve:
        student[num - 1] += 1
    print(f"before: {student}")
    # -> 방향
    for i in range(len(student) - 1):
        if student[i] > 1 and student[i+1] == 0:
            student[i] -= 1
            student[i+1] += 1
        elif student[i] == 0 and student[i+1] > 1:
            student[i] += 1
            student[i+1] -= 1
    # # <- 방향
    # for i in range(1, len(student), -1):
    #     if student[i] > 1 and student[i-1] == 0:
    #         student[i] -= 1
    #         student[i-1] += 1
    #     elif student[i] == 0 and student[i+1] > 1:
    #         student[i] += 1
    #         student[i-1] -= 1
    for i in range(len(student)):
        if student[i] >= 1:
            max_count += 1
    print(f"after: {student}")
    return max_count

    
    

