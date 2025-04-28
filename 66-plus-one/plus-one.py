class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dStr = ""
        for d in digits:
            dStr+=str(d)
        added = int(dStr)+1
        return list(map(int,str(added)))