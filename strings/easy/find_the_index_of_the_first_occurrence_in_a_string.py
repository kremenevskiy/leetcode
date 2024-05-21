class Solution(object):
    def strStr(self, haystack, needle):
        # or KMP
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)