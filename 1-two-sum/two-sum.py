class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            print()
            if target - nums[i] in hmap:
                return [hmap[target - nums[i]],i]
            hmap[nums[i]] = i