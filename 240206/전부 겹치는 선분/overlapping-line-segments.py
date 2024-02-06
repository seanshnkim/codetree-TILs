import sys
input = sys.stdin.readline

N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

def solution(segments):
    overlapped_area = segments[0]
    for x1, x2 in segments:
        tmp_start, tmp_end = 0, 0
        start, end = overlapped_area

        if (start <= x1 and x1 <= end):
            tmp_start = x1
            if x2 <= end:
                tmp_end = x2
            else:
                tmp_end = end
        elif x1 < start:
            tmp_start = x1
            if x2 < start:
                return False
            else:
                tmp_end = x2
        # x1 > end
        else:
            return False
        
        overlapped_area = tmp_start, tmp_end

    return True

if solution(segments):
    print("Yes")
else:
    print("No")