import sys
input = sys.stdin.readline
from collections import defaultdict

# 이 문제는 단순히 .sort 쓰면 시간 초과할 듯?

N, K = map(int, input().split())
nums = list(map(int, input().split()))

counts = defaultdict(int)
# counts_rev = defaultdict(list)
counts_rev = defaultdict(int)

for n in nums:
    counts[n] += 1
    
# for n, cnt in counts.items():
#     if n not in counts_rev[cnt]:
#         counts_rev[cnt].append(n)
    # counts_rev[cnt].sort()

# 해시맵은 엄밀히 말해서(최신 파이썬 버전은 지원하지만) key 값으로 정렬할 수 없으므로
# 배열로 만들어준다.
reversed_arr = []
for n, cnt in counts.items():
    reversed_arr.append((cnt, n))
# lambda 식 외워놓자(정렬 기준이 여러 개일 경우)
reversed_arr.sort(key=lambda x: (x[0], x[1]), reverse=True)

ans = []
for i in range(K):
    ans.append(reversed_arr[i][1])

print(*ans)