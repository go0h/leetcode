class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        
        left = 0
        right = 1
        diff = -1
        if len(nums) > 1:
            diff = nums[right] - nums[left]

        count = 0
        counts = [0] * len(nums)
        while right < len(nums):

            next_diff = nums[right] - nums[right - 1]
            
            if next_diff == diff:
                if right - left >= 2:
                    count += 1
                    counts[right] = count
            else:
                diff = next_diff
                left = right - 1
                count = 0

            right += 1

        return sum(counts)

if __name__ == '__main__':

    nums = [1,2,3,4]
    nums = [-1,-10]
    # nums = [1,2,3,4,5,6]
    result = Solution().numberOfArithmeticSlices(nums)

    print(result)