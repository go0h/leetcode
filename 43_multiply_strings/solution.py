class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1r = [int(num1[i]) for i in range(len(num1) - 1, -1, -1)]
        num2r = [int(num2[i]) for i in range(len(num2) - 1, -1, -1)]
        result = [0] * (len(num1) + len(num2))

        if len(num2r) > len(num1r):
            num1r, num2r = num2r, num1r

        for i in range(len(num1r)):
            for j in range(len(num2r)):
                remainder = num1r[i] * num2r[j]
                k = i + j
                while remainder > 0:
                    result[k] = result[k] + remainder % 10
                    remainder = remainder // 10 + result[k] // 10
                    result[k] = result[k] % 10
                    k += 1
        result.reverse()

        return str(int(''.join([str(i) for i in result])))

if __name__ == '__main__':

    num1 = "123"
    num2 = "456"

    result = Solution().multiply(num1, num2)
    print(result)
