class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        slow = 0
        fast = 1
        while fast < k:
            print(slow, fast, k)
            while fast < k and nums[slow] == nums[fast]:
                fast += 1
            if fast < k:
                nums[slow + 1] = nums[fast]
                slow += 1
                fast += 1
        return len(nums[:slow + 1])
