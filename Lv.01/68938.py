from collections import defaultdict
from itertools import groupby


def solution(s):
    n = len(s)
    if n == 1:
        return 0

    groups = defaultdict(lambda: defaultdict(int))
    for c, group in groupby(s):
        groups[c][len(list(group))] += 1

    answer = (n - 1) * n * (n + 1) // 6
    for group in groups.values():
        t, side = sum(l * count for l, count in group.items()), sum(group.values())
        for i in range(1, max(group) + 1):
            answer -= t * (t - 1) // 2
            t -= side
            side -= group[i]

    return answer
