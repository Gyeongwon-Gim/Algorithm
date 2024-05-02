from itertools import combinations

N = int(input())
score = []
numList = [i for i in range(N)]
cnt = N

while cnt >= 1:
   a, b = map(int, input().split())
   score.append([a, b])
   cnt-= 1

resultList = []
answer = []

sourList = 1
bitterList = 0

for i in range(1, N+1): 
   caseList = list(combinations(numList, i))

   for j in range(len(caseList)):
      for k in caseList[j]:
         # 신맛 - 곱
         sourList *= score[k][0]
         # 쓴맛 - 합
         bitterList += score[k][1]
         
         result = abs(sourList - bitterList)
         answer.append(result)
      # 초기화
      sourList = 1
      bitterList = 0

print(min(answer))