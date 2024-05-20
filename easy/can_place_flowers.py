class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        flowerbed += [0]
        prev = 0
        if n == 0:
            return True
        for i in range(l):
            if prev == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break
            prev = flowerbed[i]
        return n == 0



flowerbed = [1,0,0,0,1]
n = 1
ans = True
assert Solution().canPlaceFlowers(flowerbed, n) == ans


flowerbed = [1,0,0,0,1]
n = 2
ans = False
assert Solution().canPlaceFlowers(flowerbed, n) == ans