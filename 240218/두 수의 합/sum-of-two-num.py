import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
_dict = defaultdict(int)
for n in nums:
    _dict[n] += 1

ans = 0
for n in nums:
    if _dict[n] == 0 or _dict[K-n] == 0:
        continue
    if n == K -n:
        ans += _dict[n] * (_dict[n]- 1) // 2
        _dict[n] = 0
    else:
        ans += _dict[n] * _dict[K-n]
        _dict[n] -= 1

# print(_dict)
print(ans)