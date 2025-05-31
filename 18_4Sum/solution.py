class Solution:
    
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        def twoSum(nums: list[int], target: int) -> list[int]:
            dp = dict()
            result = []
            for i in range(len(nums)):

                if target - nums[i] in dp:
                    # print([nums[dp[target - nums[i]]], nums[i]])
                    result.append([nums[dp[target - nums[i]]], nums[i]])
                
                dp[nums[i]] = dp.get(nums[i], i)
                
            return result
  
        nums.sort()

        print(nums)

        result = []
        first = 0
        while first < len(nums):

            second = first + 1

            while second < len(nums):

                print(nums[first], nums[second], nums[second + 1 : len(nums)])

                two_sums = twoSum(
                        nums[second + 1 : len(nums)], 
                        (target - (nums[first] + nums[second]))
                    )

                for two_sum in two_sums:
                    quadruple = [nums[first], nums[second]] + two_sum
                    print(quadruple)
                    if len(quadruple) == 4 and quadruple not in result:
                        result.append(quadruple)

                second += 1

            first += 1
        
        return list(result)

if __name__ == '__main__':

    nums = [1,0,-1,0,-2,2]
    nums = [2,4,0,4,-3,-3]
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0

    result = Solution().fourSum(nums, target)

    print(result)