class Solution:
    def fib(self, n: int) -> int:
        """
        def fib(self, n: int) -> int:
            Returns the fibonacci number of `n`.

        :param n int: number `n` should be positive integer
        :exception: ValueError, TypeError
        :rtype: int
        :return: fib(n)
        """

        if n < 0:
            raise ValueError(f"{n=}, n must be greater than zero")

        if not isinstance(n, int):
            raise TypeError(f"{type(n)} is not type int, use type int instead")
        
        if n == 0: return 0

        n1, n2 = 0, 1

        for i in range(1, n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3

        return n2        
