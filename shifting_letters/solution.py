class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:

        sum = 0
        result = [(ord(c) - 97) for c in s]
        for i in range(len(s) - 1, -1, -1):
            sum += shifts[i]
            result[i] = (result[i] + sum) % 26

        return ''.join([chr(num + 97) for num in result])


if __name__ == '__main__':

    s = "aaa"
    shifts = [1,2,3]
    result = Solution().shiftingLetters(s, shifts)
    print(result)