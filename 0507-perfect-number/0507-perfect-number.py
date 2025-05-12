class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        def checkPerfectNumber(self, num: int) -> bool:
            Returns true if num is Perfect Number

        :param num int: number num should be positive integer
        :exceptions: TypeError
        :rtype: bool
        :return: perfect number of num
        """

        if not isinstance(num, int): 
            raise TypeError(num, 'is not type int, use type int instead')

        if num <= 1: return False

        sum = 1
        sqrtNum = int(math.sqrt(num))

        for i in range(2, sqrtNum+1):
            if num%i == 0:
                sum += i
                if i != num/i: 
                    sum += num/i

        return num == sum
