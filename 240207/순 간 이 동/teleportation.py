import sys
input = sys.stdin.readline

A, B, x, y = map(int, input().split())
ans = 0

Ax_diff = abs(A - x)
Ay_diff = abs(A - y)
Bx_diff = abs(x - B)
By_diff = abs(y - B)
Ax_to_yB = abs(A - x) + abs(y - B)
Ay_to_xB = abs(A - y) + abs(x - B)

dist = abs(B - A)
ans = dist

if Ax_to_yB < dist or Ay_to_xB < dist:
    if Ax_to_yB < Ay_to_xB:
        ans = Ax_to_yB
    else:
        ans = Ay_to_xB

print(ans)