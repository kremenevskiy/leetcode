class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n - 1
        m, n = m-1, n-1
        while cur >= 0:
            num1 = nums1[m] if m >= 0 else None
            num2 = nums2[n] if n >= 0 else None
            if num1 is not None and num2 is not None:
                if num1 > num2:
                    nums1[cur] = num1
                    m -= 1
                else:
                    nums1[cur] = num2
                    n -= 1
            else:
                if num1 is not None:
                    nums1[cur] = num1
                    m -= 1
                else:
                    nums1[cur] = num2
                    n -= 1
            cur -=1


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        last = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
assert nums1 == [1,2,2,3,5,6]


nums1 = [1]
m = 1
nums2 = []
n = 0
Solution().merge(nums1, m, nums2, n)
assert nums1 == [1]



nums1 = [0]
m = 0
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)
assert nums1 == [1]


nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
Solution().merge(nums1, m, nums2, n)
assert nums1 == [-1,0,0,1,2,2,3,3,3]


