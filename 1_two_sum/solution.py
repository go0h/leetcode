class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        dp = dict()
        for i in range(len(nums)):

            if target - nums[i] in dp:
                return [dp[target - nums[i]], i]
            
            dp[nums[i]] = dp.get(nums[i], i)
            
        return None

if __name__ == '__main__':

    nums = [2,7,11,15]
    target = 9

    nums = [3,2,4]
    target = 6

    print(nums)
    result = Solution().twoSum(nums, target)
    print(result)