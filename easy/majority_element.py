class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return nums[len(nums)//2]


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major, count = nums[0], 1
        for num in nums[1:]:
            if num == major:
                count += 1
            else:
                if count == 1:
                    major, count = num, 1
                else:
                    count -= 1
            if count > len(nums) // 2:
                break
        return major

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major, count = 0, 0
        for num in nums:
            if count == 0:
                major = num
            if num == major:
                count += 1
            else:
                count -= 1
        return major
    

            
        
nums = [3,2,3]
ans = 3
assert Solution().majorityElement(nums) == ans


nums = [2,2,1,1,1,2,2]
ans = 2
assert Solution().majorityElement(nums) == ans