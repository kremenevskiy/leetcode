class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rem = 1
        for i in range(len(digits)-1, -1, -1):
            print(digits, i)
            if digits[i] + rem == 10:
                digits[i] = 0
                rem = 1
            else:
                digits[i] = digits[i] + rem
                rem = 0
                break
        return [1] + digits if rem == 1 else digits
        
        
digits = [1,2,3]
ans = [1,2,4]
assert Solution().plusOne(digits) == ans

digits = [4,3,2,1]
ans = [4,3,2,2]
assert Solution().plusOne(digits) == ans

digits = [9]
ans = [1, 0]
assert Solution().plusOne(digits) == ans
        