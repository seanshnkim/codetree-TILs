import sys
input = sys.stdin.readline

N = int(input())
count = {}
for i in range(N):
    S = input().rstrip('\n')
    S_sorted = ''.join(sorted(S))
    if S_sorted in count:
        count[S_sorted] += 1
    else:
        count[S_sorted] = 1

print(max(count.values()))