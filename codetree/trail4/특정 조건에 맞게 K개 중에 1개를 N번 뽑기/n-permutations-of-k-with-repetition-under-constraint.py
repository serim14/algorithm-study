K, N = map(int, input().split())

answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    # 종료조건
    if curr_num == N+1:
        print_answer()
        return

    for num in range(1, K+1):
        if curr_num >= 3 and num == answer[-1] and num == answer[-2]:
            continue
        answer.append(num)
        choose(curr_num+1)
        answer.pop()


choose(1)
