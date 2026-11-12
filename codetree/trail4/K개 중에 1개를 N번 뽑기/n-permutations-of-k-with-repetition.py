# 1이상 K이하의 정수를 하나 고르는 행위를
# N번반복하여 나올 수 있는
# 서로 다른 수열 구하기

K, N = map(int, input().split())

answer = []
temp = []

def print_answer():
    for i in range(len(answer)-N+1):
        for j in range(N):
            print(answer[i+j], end=" ")
        print()


# 수를 1개 고르는 함수 정의
def choose(curr_num):
    # 종료 조건
    if curr_num >= N:
        print_answer()
        return
    
    for i in range(1, K+1):
        answer.append(i)
        choose(curr_num+1)
        answer.pop()


choose(0)



