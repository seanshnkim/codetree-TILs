import sys
input = sys.stdin.readline
from sortedcontainers import SortedDict

N = int(input())
my_treemap = SortedDict()
for _ in range(N):
    args = input().split()
    command = args[0]
    if command == "add":
        k, v = map(int, args[1:])
        my_treemap[k] = v
    elif command == "remove":
        k = int(args[1])
        del my_treemap[k]
    elif command == "find":
        k = int(args[1])
        if k in my_treemap:
            print(my_treemap[k])
        else:
            print(None)
    elif command == "print_list":
        # if is not empty
        if my_treemap:
            # 이렇게 하면 key 기준으로 정렬되지 않는다... Why?
            print(*my_treemap.values())
        else:
            print(None)