N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

# 우 하
dx = [1, 0]
dy = [0, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def can_go(x, y):
    # 격자 안인지
    if in_range(x, y):
        if not visited[x][y] and board[x][y]  == 1:# 방문한 적 없고, 뱀이 없는지
            return True
    
    return False


# 이 함수에서는 계속해서 이동가능한 곳 찾아서 가기
def dfs(x, y):
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)



visited[0][0] = 1
dfs(0, 0)

print(visited[N-1][M-1])