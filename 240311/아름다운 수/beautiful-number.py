import sys
input = sys.stdin.readline

N = int(input())
# def repeat_ver1(prev, cnt, num_str):
#     if len(num_str) == 0:
#         if prev == '1':
#             return True
#         elif prev == '2':
#             if cnt % 2 == 0:
#                 return True
#             else:
#                 return False
#     if prev == '1':
#         repeat(num_str[0], 1, num_str[1:])
#     elif prev == '2':
#         if cnt % 2 == 0:
#             if num_str[0] == '2':
#                 repeat(num_str[0], cnt+1, num_str[1:])
#             else:
#                 repeat(num_str[0], 1, num_str[1:])
#         else:
#             if num_str[0] == '2':
#                 repeat(num_str[0], cnt+1, num_str[1:])
#             else:
#                 return False

ans = 0
def repeat(start, cnt, n):
    if n == 0:
        if (start == 1) or \
           (start == 2 and cnt % 2 == 0) or \
           (start == 3 and cnt % 3 == 0) or \
           (start == 4 and cnt % 4 == 0):
            global ans
            ans += 1
        return
            
    if start == 1:
        for i in range(1, 5):
            repeat(i, 1, n-1)
    elif start == 2:
        # 만약 2의 현재 누적 개수가 2, 4, 6...이라면
        if cnt % 2 == 0:
            for i in range(1, 5):
                repeat(i, 1, n-1)
        # 만약 2의 현재 누적 개수가 1, 3, 5...이라면
        else:
            # 2가 다음에 최소 1개 등장해야만 '아름다운 수' 조건이 성립한다.
            repeat(2, cnt+1, n-1)
    elif start == 3:
        # 만약 3의 현재 누적 개수가 3, 6, 9...이라면
        if cnt % 3 == 0:
            for i in range(1, 5):
                repeat(i, 1, n-1)
        else:
            repeat(3, cnt+1, n-1)

for i in range(1, 5):
    repeat(i, 1, N-1)

print(ans)