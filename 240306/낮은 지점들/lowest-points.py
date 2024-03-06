import sys
input = sys.stdin.readline

N = int(input())
coordinates = {}

for _ in range(N):
    x, y = map(int, input().split())
    if x not in coordinates:
        coordinates[x] = y
    else:
        if y < coordinates[x]:
            coordinates[x] = y

ans = sum(coordinates.values())
print(ans)