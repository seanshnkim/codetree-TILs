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
    ans += _dict[K-n]

# 4 입장에서 5를 골랐을 때 1번, 5 입장에서 4를 골랐을 때 1번
# -> 2번으로 count되지만 사실 두 개 수의 골라 합이 k가 되는 경우는 1가지이므로
# 항상 2로 나눠주어야 한다.
print(ans // 2)