class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        remainder = abs(dividend)
        u_divisor = abs(divisor)

        while remainder >= u_divisor:
            remainder -= u_divisor
            result += 1
        sign = 1
        if dividend < 0 and divisor < 0:
            sign = 1
        elif dividend < 0 or divisor < 0:
            sign = -1
        return result * sign
