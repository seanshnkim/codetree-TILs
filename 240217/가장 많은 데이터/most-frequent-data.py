import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
_dict = defaultdict(int)
for _ in range(N):
    s = input()
    _dict[s] += 1

print(max(dict.values()))