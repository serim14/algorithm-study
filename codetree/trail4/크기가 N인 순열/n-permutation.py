# 1부터 N까지의 수 정확히 한 번씩만 사용하여 만들 수 있는 가능한 모든 수열

N = int(input())

visited = [False] * (N+1)
answer = []

# 수열은 순서 신경쓴다 !

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    # 종료 조건
    if curr_num == N+1:
        print_answer()
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)

        choose(curr_num+1)

        answer.pop()
        visited[i] = False

choose(1)