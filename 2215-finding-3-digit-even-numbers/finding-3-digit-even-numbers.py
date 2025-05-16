from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        seen = set()
        for p in permutations(digits, 3):
            if p[0] != 0 and p[2] % 2 == 0:
                num = 100 * p[0] + 10 * p[1] + p[2]
                seen.add(num)  # set handles duplicates fast
        return sorted(seen)
