class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_pos = 0
        num_position = 0
        if len(nums) <= 1:
            return nums

        
        while (zero_pos < n) and (num_position < n):
            # search zero pos
            # print(nums)

            while nums[zero_pos] != 0:
                zero_pos += 1
                if zero_pos >= n:
                    return nums
            # search nums pos
            while nums[num_position] == 0:
                num_position += 1
                if num_position >= n:
                    return nums
            if zero_pos > num_position:
                num_position += 1
                continue
            nums[num_position], nums[zero_pos] = nums[zero_pos], nums[num_position]
            zero_pos += 1
            num_position += 1
        return nums
            

class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums

             


nums = [0, 1, 0, 3, 12]
ans = [1,3,12,0,0]
assert Solution().moveZeroes(nums) == ans


nums = [0]
ans = [0]
assert Solution().moveZeroes(nums) == ans


nums = [1,0]
ans = [1,0]
assert Solution().moveZeroes(nums) == ans
