import sys
input = sys.stdin.readline

N, K = map(int, input().split())
changes = [tuple(map(int, input().split())) for _ in range(K)]

seats = [i for i in range(N+1)]

# records = [set() for _ in range(N+1)]
# 처음 앉아있는 자리(1번 사람은 1, 2번 사람은 2...)를 더하지 않아서 틀렸다
records = [set([i]) for i in range(N+1)]

for k in range(3):
    for change in changes:
        ai, bi = change
        # records[seats[ai]].add(seats[bi])
        # records[seats[bi]].add(seats[bi])
        records[seats[ai]].add(bi)
        records[seats[bi]].add(ai)
        seats[bi], seats[ai] = seats[ai], seats[bi]
        # print(seats)

# print(records)

for i in range(1, N+1):
    print(len(records[i]))