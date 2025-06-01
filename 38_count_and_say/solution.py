class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def convert2RLE(s):
            result = []
            cnt = 1
            prev = s[0]
            for i in range(1, len(s)):
                if s[i] != prev:
                    result.append(str(cnt) + prev)
                    prev = s[i]
                    cnt = 1
                else:
                    cnt += 1
            result.append(str(cnt) + prev)
            return ''.join(result)

        if n == 1:
            return "1"

        return convert2RLE(self.countAndSay(n - 1))

if __name__ == '__main__':

    target = 6

    result = Solution().countAndSay(target)
    print(result)

    # countAndSay(1) = "1"
    # countAndSay(2) = RLE of "1" = "11"
    # countAndSay(3) = RLE of "11" = "21"
    # countAndSay(4) = RLE of "21" = "1211"
    # countAndSay(5) = RLE of "21" = "21211"
