import sys
input = sys.stdin.readline

numA, numB = map(int, input().split())
setA = set(list(map(int, input().split())))
setB = set(list(map(int, input().split())))

symmetric_diff = setA.union(setB) - setA.intersection(setB)
print(len(symmetric_diff))