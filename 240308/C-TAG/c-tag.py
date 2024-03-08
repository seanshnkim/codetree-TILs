import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
groupA = [input().rstrip('\n') for _ in range(N)]
groupB = [input().rstrip('\n') for _ in range(N)]

# 그룹 A에 대한, 구분 기준이 되는 세자리의 조합들
setA = set()
# 그룹 B에 대한, 구분 기준이 되는 세자리의 조합들
setB = set()
ans = 0

for comb in combinations(range(M), 3):
    # 비워줘야 한다.
    setA.clear()
    setB.clear()

    i1, i2, i3 = comb
    for strA in groupA:
        # 알파벳 순서가 달라진다고 다르게 구분하는가? 그건 아닌 듯.
        listA = sorted([strA[i1], strA[i2], strA[i3]])
        tupA = tuple(listA)
        # tuple, 즉 조합 그 자체를 하나의 원소로 집합에 더해야 한다.
        setA.add(tupA)
    for strB in groupB:
        listB = sorted([strB[i1], strB[i2], strB[i3]])
        tupB = tuple(listB)
        setB.add(tupB)
    # 두 집합 간의 교집합이 존재하지 않는다면, 
    # 즉 그룹A와 그룹B가 완벽히 다르게 구분된다면
    if not setA.intersection(setB):
        ans += 1

print(ans)