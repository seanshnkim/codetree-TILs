import sys
input = sys.stdin.readline

N = int(input())

ans = 0
def repeat(start, cnt, n, cur_str):
    if n == 0:
        if cnt % start == 0:
            global ans
            ans += 1
            # print(cur_str)
        return
    
    if cnt % start == 0:
        for i in range(1, 5):
            repeat(i, 1, n-1, cur_str+str(i))
    else:
        repeat(start, cnt+1, n-1, cur_str+str(start))
        
    # if start == 1:
    #     for i in range(1, 5):
    #         repeat(i, 1, n-1, cur_str+str(i))
    # elif start == 2:
    #     # 만약 2의 현재 누적 개수가 2, 4, 6...이라면
    #     if cnt % 2 == 0:
    #         for i in range(1, 5):
    #             repeat(i, 1, n-1, cur_str+str(i))
    #     # 만약 2의 현재 누적 개수가 1, 3, 5...이라면
    #     else:
    #         # 2가 다음에 최소 1개 등장해야만 '아름다운 수' 조건이 성립한다.
    #         repeat(2, cnt+1, n-1, cur_str+str(2))
    # elif start == 3:
    #     # 만약 3의 현재 누적 개수가 3, 6, 9...이라면
    #     if cnt % 3 == 0:
    #         for i in range(1, 5):
    #             repeat(i, 1, n-1, cur_str+str(i))
    #     else:
    #         repeat(3, cnt+1, n-1, cur_str+str(3))
    # # start == 4:
    # else:
    #     if cnt % 4 == 0:
    #         for i in range(1, 5):
    #             repeat(i, 1, n-1, cur_str+str(i))
    #     else:
    #         repeat(4, cnt+1, n-1, cur_str+str(4))

for i in range(1, 5):
    repeat(i, 1, N-1, str(i))

print(ans)