class Solution:
    
    def myAtoi(self, s: str) -> int:

        res = 0
        sign = 1
        start_pos = 0

        s1 = s.strip()

        limit = 2 ** 31
        
        if s1[0] == '-':
            sign = -1
            start_pos = 1
        elif s1[0] == '+':
            start_pos = 1

        for i in range(start_pos, len(s1)):
            if not s1[i].isdigit():
                break
            res = res * 10 + int(s1[i])

            if res > limit:
                res = limit

        return res * sign

if __name__ == '__main__':

    print(str(Solution().myAtoi("-91283472332")))
