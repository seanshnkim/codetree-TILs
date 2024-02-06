import sys

INT_MAX = sys.maxsize

N = int(input())

max_x1 = 0
min_x2 = INT_MAX
x1s, x2s = [], []

for _ in range(N):
    x1, x2 = tuple(map(int, input().split()))
    x1s.append(x1)
    x2s.append(x2)

is_overlapping = False
for n in range(N):
    out_x1, out_x2 = x1s[n], x2s[n]
    max_x1 = max(x1s)
    min_x2 = min(x2s)

    if out_x1 == max(x1s):
        x1s.remove(out_x1)
        max_x1 = max(x1s)
    if out_x2 == min(x2s):
        x2s.remove(out_x2)
        min_x2 = min(x2s)
    
    if min_x2 >= max_x1:
        is_overlapping = True
        break

    x1s.append(out_x1)
    x2s.append(out_x2)

if is_overlapping:
    print("Yes")
else:
    print("No")