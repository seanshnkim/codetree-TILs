import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))

_dict = defaultdict(int)
for n in nums:
    _dict[n] += 1

print(*[_dict[q] for q in queries])