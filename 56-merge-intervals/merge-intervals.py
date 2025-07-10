class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval = sorted(intervals)

        newlist = [interval[0]]

        for i in range(1,len(intervals)):
            if interval[i][0] <= newlist[-1][1]:
                newlist[-1][1] = max(interval[i][1], newlist[-1][1])
            else:
                newlist.append(interval[i])
        return newlist
