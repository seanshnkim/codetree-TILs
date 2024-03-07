import sys
input = sys.stdin.readline
from sortedcontainers import SortedDict

N = int(input())
sd = SortedDict()
for _ in range(N):
    word = input().rstrip('\n')
    if word not in sd:
        sd[word] = 1
    else:
        sd[word] += 1

for word, cnt in sd.items():
    print(word, cnt)