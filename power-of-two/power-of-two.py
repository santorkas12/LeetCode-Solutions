class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)