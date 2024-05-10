class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer = 0
        mx_val = nums[-1] # just for speed up
        for i in range(1, len(nums)):
            if nums[i] != nums[pointer]:
                pointer += 1    
                nums[pointer] = nums[i]
            if mx_val == nums[pointer]:
                break
        return pointer + 1

nums = [1,1,2,2,3,3,4,4,4,4,4,5]
Solution().removeDuplicates(nums)
print(nums)