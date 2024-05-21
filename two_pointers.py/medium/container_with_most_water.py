class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right = 0, len(height) - 1
        mx_area = (right - left) * min(height[left], height[right])
        tallest = max(height)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            print(left, right)
            mx_area = max(mx_area, (right - left) * min(height[left], height[right]))
            if mx_area > (right - left) * tallest:
                break
        return mx_area
            

height = [1,8,6,2,5,4,8,3,7]
ans = 49
assert Solution().maxArea(height) == ans

height = [1,1]
ans = 1
assert Solution().maxArea(height) == ans