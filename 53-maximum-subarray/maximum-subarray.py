class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = max_sum = nums[0]

        for i in range(1,len(nums)):
            currsum = max(nums[i], currsum + nums[i])
            max_sum = max(max_sum, currsum)
        return max_sum
        