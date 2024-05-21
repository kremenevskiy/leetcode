import itertools
from collections import defaultdict
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for pair in list(itertools.product(nums1, nums2)):
            hash1[pair[0] + pair[1]] += 1
        for pair in list(itertools.product(nums3, nums4)):
            hash2[pair[0] + pair[1]] += 1

        ans = 0
        for k1, v1 in hash1.items():
            for k2, v2 in hash2.items():
                if k1 + k2 == 0:
                    ans += v1 * v2
        return ans


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        ans = 0
        for pair in list(itertools.product(nums1, nums2)):
            hash1[pair[0] + pair[1]] += 1
        for pair in list(itertools.product(nums3, nums4)):
            new_val = pair[0] + pair[1]
            if -new_val in hash1:
                ans += hash1[-new_val]
        return ans
    
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hash1 = defaultdict(int)
        ans = 0
        for a in nums1:
            for b in nums2:
                hash1[a + b] += 1
        for c in nums3:
            for d in nums4:
                new_val = c + d
                if -new_val in hash1:
                    ans += hash1[-new_val]
        return ans

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hash1 = defaultdict(int)
        ans = 0
        for a in nums1:
            for b in nums2:
                hash1[a + b] += 1
        for c in nums3:
            for d in nums4:
                ans += hash1[-c-d]
        return ans

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
ans = 2
assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == ans


nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
ans = 1
assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == ans


nums1 = [-1, -1]
nums2 = [-1, 1]
nums3 = [-1, 1]
nums4 = [1, -1]
ans = 6
assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == ans