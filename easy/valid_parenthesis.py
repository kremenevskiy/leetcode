b = {
    '(': ')',
    '[': ']',
    '{': '}'
}

class Solution(object):
    def isValid(self, s):
        stack = []
        for br in s:
            if br in '{([':
               stack.append(br)
               continue
            elif not stack or b[stack.pop()] != br:
                return False
        return len(stack) == 0


s = "()"
ans = True
assert Solution().isValid(s) == ans

s = "()[]{}"
ans = True
assert Solution().isValid(s) == ans

s = "(]"
ans = False
assert Solution().isValid(s) == ans