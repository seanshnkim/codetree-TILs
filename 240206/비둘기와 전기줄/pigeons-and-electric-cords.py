import sys
input = sys.stdin.readline

N = int(input())
locations = [tuple(map(int, input().split())) for _ in range(N)]
cnt = 0
observed = dict()

for idx, cur_side in locations:
    if idx in observed:
        prev_side = observed[idx]
        if cur_side != prev_side:
            cnt += 1
            observed[idx] = cur_side
    else:
        observed[idx] = cur_side

print(cnt)