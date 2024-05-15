class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        pass



def func(index):
    i = 1
    while True:
        if index == 1:
            break
        i += 1
        yield i


gen = func(4)

t = next(gen)
print(t)


