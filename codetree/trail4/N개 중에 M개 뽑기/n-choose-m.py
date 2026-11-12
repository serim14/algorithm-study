# 1이상 N이하 정수 중 M개의 정수 골라 만들 수 있는 모든 조합
# 오름차수 정렬

N, M = map(int, input().split())

answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()


# 몇번째 수를 뽑고 있는지, 전에 뽑은 숫자보다 큰 숫자 뽑기
def choose(curr_num, start):
    # 종료 조건
    if curr_num == M+1:
        print_answer()
        return
    
    for i in range(start, N+1):
        answer.append(i)
        choose(curr_num+1, i+1)
        answer.pop()

choose(1, 1)