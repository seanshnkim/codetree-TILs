import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0
for r in range(N-2):
    for c in range(N-2):
        cnt = sum(sum(grid[r+k][c:c+3]) for k in range(3))
        max_cnt = max(max_cnt, cnt)
print(max_cnt)