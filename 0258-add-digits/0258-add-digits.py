class Solution:
    def addDigits(self, num: int) -> int:
        """
        def addDigits(self, num: int) -> int:
            Returns the added digit of num upto single unit.

        :param num int: number must be positive integer
        :exception: 
        :rtype: int
        :return: addDigit(num)
        """

        if num<0:
            num = abs(num)

        if not isinstance(num, int):
            raise TypeError(type(num), "is not type int, use type int instead.")

        if num < 0:
            return ValueError(f"{num=} is not valid number.")

        return 0 if num==0 else 1 + (num - 1) % 9
        