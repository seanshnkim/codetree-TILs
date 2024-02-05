import sys
input = sys.stdin.readline

x1, x2 = map(int, input().split())
a1, a2 = map(int, input().split())

if a1 >= x1 and a1 <= x2:
    if a2 > x2:
        print(a1 - x1 + a2 - a1)
    else:
        print(x2 - x1)
elif x1 >= a1 and x1 <= a2:
    if x2 > a2:
        print(x1-a1 + x2-x1)
    else:
        print(a2 - a1)
else:
    # if a2 <= x1 or x2 <= a1:
    print(x2-x1 + a2-a1)