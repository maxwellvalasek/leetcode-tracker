class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = len(nums)
        slow = 0
        fast = 1
        while fast < k:
            if nums[slow] == 0:
                if nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
                    fast = slow + 1
                else:
                    fast += 1
            else:
                slow += 1
                fast = slow + 1  # <- fix: align fast with new slow
