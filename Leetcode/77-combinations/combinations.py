import itertools

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        items = [x for x in range(1,n+1)]
        combos = itertools.combinations(items,k)
        return list(combos)