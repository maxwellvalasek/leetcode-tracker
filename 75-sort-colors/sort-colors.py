class Solution:
    from collections import defaultdict
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hmap = defaultdict(int)
        for num in nums:
            hmap[num]+=1
        print(hmap)


        for i in range(hmap[0]):
            nums[i] = 0
        for i in range(hmap[1]):
            nums[i+hmap[0]] = 1
        for i in range(hmap[2]):
            nums[i+hmap[0]+hmap[1]] = 2
        #for i in range(len(nums)):
