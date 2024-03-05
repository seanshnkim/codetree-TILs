import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))

_dict = dict()
for n in nums:
    if n in _dict:
        _dict[n] += 1
    else:
        _dict[n] = 1

ans = []
for q in queries:
    if q in _dict:
        ans.append(_dict[q])
    else:
        ans.append(0)
print(*ans)