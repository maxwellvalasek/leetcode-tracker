class Solution:
    from collections import Counter
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int: 
        count = 0
        newdom = []
        for domino in dominoes:
            domino.sort()
            domino = ''.join(str(dom) for dom in domino)
            newdom.append(domino)

        print(newdom)
        mcount = Counter(newdom)
        print(mcount)
        for val in mcount.values():
            if val >=2:
                count += (val * (val-1))//2
        return count
