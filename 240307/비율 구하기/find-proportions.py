import sys
input = sys.stdin.readline
from sortedcontainers import SortedDict

sd = SortedDict()
N = int(input())
for _ in range(N):
    S = input().rstrip('\n')
    if S in sd:
        sd[S] += 1
    else:
        sd[S] = 1

for S, cnt in sd.items():
    # print(S, round(cnt/N*100, 4))
    ratio = cnt/N*100
    print(f"{S} {ratio:.4f}")