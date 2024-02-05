import sys
input = sys.stdin.readline

x1, x2, x3, x4 = map(int, input().split())

# x2 < x3
# x2 >= x3 but x2 < x4
# x2 > x4

if x2 > x4:
    if x1 <= x4:
        print("intersecting")
    else:
        print("nonintersecting")
else:
    if x3 <= x2:
        print("intersecting")
    else:
        print("nonintersecting")