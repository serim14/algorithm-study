# 1이상 N이하 정수, M개 정수 만드는 조합
# 순서는 상관 없어서 중복 제외해야겠지

N, M = map(int, input().split())

answer = []

# 조합
# 한 조합 내, 오름차순
# 전체도 오름차순으로 출력



def choose(curr_num, start):
    # 종료 조건
    if curr_num == M+1:
        for elem in answer:
            print(elem, end=" ")
        print()
        return

    for i in range(start, N+1):
        answer.append(i)
        choose(curr_num+1, i+1)
        answer.pop()

choose(1, 1)

