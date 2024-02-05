import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

if x1 < x2:
    small_x = x1
    big_x = x2
else:
    small_x = x2
    big_x = x1

if a1 < a2:
    small_a = a1
    big_a = a2
else:
    small_a = a2
    big_a = a1

####################
if y1 < y2:
    small_y = y1
    big_y = y2
else:
    small_y = y2
    big_y = y1

if b1 < b2:
    small_b = b1
    big_b = b2
else:
    small_b = b2
    big_b = b1

ans = "overlapping"

if big_x < small_a:
    ans = "nonoverlapping"
elif big_a < small_x:
    ans = "nonoverlapping"

if big_y < small_b:
    ans = "nonoverlapping"
elif big_b < small_y:
    ans = "nonoverlapping"

print(ans)


# if x1 < x2 and y1 < y2:
#     if a1 < a2 and b1 < b2:
#         if x2 < a1:
#             print("nonoverlapping")
#         elif y1 > b2:
#             print("nonoverlapping")
#     if a1 < a2 and b1 > b2:
#         if x2 < a1:
#             print("nonoverlapping")
#         elif y1 > b1:
#             print("nonoverlapping")
#     if a1 > a2 and b1 < b2:
#         if x2 < a2:
#             print("nonoverlapping")
#         elif y1 > b2:
#             print("nonoverlapping")
#     if a1 > a2 and b1 > b2:
#         if x2 < a2:
#             print("nonoverlapping")
#         elif y1 > b1:
#             print("nonoverlapping")
# elif