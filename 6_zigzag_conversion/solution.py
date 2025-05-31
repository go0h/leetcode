class Solution:
    def convert(self, s: str, numRows: int) -> str:

        columns = len(s) // (numRows - max(numRows - 2, 0)) + 1
        result = [['' for _ in range(columns) ] for _ in range(numRows)]

        row = 0
        col = 0
        i = 0
        while i < len(s):

            # down
            while row < numRows and col < columns and i < len(s):
                result[row][col] = s[i]
                row += 1
                i += 1

            col += 1
            row -= 2

            # up-right
            while row > 0 and col < columns and i < len(s):
                result[row][col] = s[i]
                col += 1
                row -= 1
                i += 1
            row = 0

        ''.startswith

        return ''.join([''.join(row) for row in result])

if __name__ == '__main__':

    s = "PAYPALISHIRING"
    n = 3

    # P   A   H   N
    # A P L S I I G
    # Y   I   R
    s = "A"
    n = 1
    print(s)
    # print("PAHNAPLSIIGYIR")
    result = Solution().convert(s, 3)
    print(result)