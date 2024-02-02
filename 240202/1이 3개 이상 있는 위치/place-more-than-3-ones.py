import sys
input = sys.stdin.readline

# 격자!
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

N = int(input())
board = []
for r in range(N):
    board.append(list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

ans = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for d in range(4):
            dx, dy = dxs[d], dys[d]
            if in_range(r+dx, c+dy) and board[r+dx][c+dy] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)