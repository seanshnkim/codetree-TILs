import sys
input = sys.stdin.readline

N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]


def solution(N, segments):
    existing_area = []
    existing_area.append(segments[0])

    for x1, x2 in segments:
        for start, end in existing_area:
            if (start <= x1 and x1 <= end) or (start <= x2 and x2 <= end):
                return "Yes"
                
        existing_area.append((x1, x2))
    
    return "No"


print(solution(N, segments))