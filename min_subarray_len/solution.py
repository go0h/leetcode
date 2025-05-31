
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = 2 ** 32
        sum = 0
        left = 0

        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                sum -= nums[left]
                left += 1
        
        return 0 if min_len == 2 ** 32 else min_len

if __name__ == '__main__':

    target = 7
    nums = [2,3,1,2,4,3]

    res = Solution().minSubArrayLen(target, nums)

    print(res)