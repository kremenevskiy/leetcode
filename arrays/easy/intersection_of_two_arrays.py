from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = defaultdict(int)
        ans = []
        for n in nums1:
            m[n] += 1
        for n in nums2:
            if n in m:
                if m[n] > 0:
                    ans.append(n)
                    m[n] -= 1
        return ans
        


nums1 = [1,2,2,1]
nums2 = [2,2]
ans = [2,2]
assert Solution().intersect(nums1, nums2) == ans


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
ans = [4,9]
ans2 = [9,4]
assert Solution().intersect(nums1, nums2) in [ans, ans2]