class Solution:

    # 0 <= i < j < n

    # nums[i] == nums[j]
    # (i * j) % k == 0

    # nums = [3,1,2,2,2,1,3], k = 2
    # 0,6 
    # 2,3 
    # 2,4 
    # 3,4
    from collections import defaultdict
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hmap = defaultdict(list)
        count = 0
        for i, val in enumerate(nums):

            hmap[val] += [i]
        
        for key, value in hmap.items():
            print(key,value)
            if len(value) >= 2:
                for i in range(len(value)):
                    for j in range(i + 1, len(value)):
                        if (value[i]* value[j]) % k == 0:
                            count+=1
                
        return count


        