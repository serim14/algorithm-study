# N개의 집
# i번째 집에는 Ai명의 사람이 삶
# 회의를 위해 N개의 집 중 한 곳에 전부 모이려고 함
# 적절한 집을 선택하여 모든 사람들의 이동 거리의 합이 최소가 되도록 작성

N = int(input())

num_of_people = list(map(int, input().split()))

min_dis = float("inf")

# 먼저 집 한 개를 선택하자
for i in range(N):
    # 모든 사람들의 이동 거리 계산
    distance = 0
    for j in range(N):
        if i != j:
            distance += abs(i-j)*num_of_people[j]
    
    min_dis = min(min_dis, distance)

print(min_dis)


