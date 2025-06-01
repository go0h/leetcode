class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min_num = 2**32 - 1
        max_num = 0
        seen = dict()
        for num in nums:
            if num < 1:
                continue
            if min_num > num:
                min_num = num
            if max_num < num:
                max_num = num
            seen[num] = True

        if min_num > 1:
            return 1

        for num in range(min_num + 1, max_num + 2):
            if seen.get(num, False) == False:
                return num

        return max_num + 1

if __name__ == '__main__':

    nums = [1,2,0]

    result = Solution().firstMissingPositive(nums)
    print(result)
