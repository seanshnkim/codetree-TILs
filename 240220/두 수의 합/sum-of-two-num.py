import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
count = defaultdict(int)
for n in nums:
    count[n] += 1

ans = 0
for n in nums:
    if count[n] == 0 or count[K-n] == 0:
        continue
    if n == K-n:
        ans += count[n] * (count[n]- 1) // 2
        count[n] = 0
    else:
        ans += count[n] * count[K-n]
        count[n] -= count[K-n]

print(ans)