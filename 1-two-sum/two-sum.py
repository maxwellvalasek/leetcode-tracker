class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in hmap:
                return [hmap[target-nums[i]],i]
            hmap[nums[i]] = i
