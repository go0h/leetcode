class Solution:

    def threeSumClosest(self, nums: list[int], target: int) -> int:

        min_diff = float('inf')
        closest = max(nums)
        nums.sort()
    
        print(nums)

        for i in range(len(nums)):

            j = i + 1
            k = len(nums) - 1
            while j < k:

                print(nums[i], nums[j], nums[k])

                cur_sum = nums[i] + nums[j] + nums[k]

                if cur_sum == target:
                    return target
                elif abs(target - cur_sum) < min_diff:
                    min_diff = abs(target - cur_sum) 
                    closest = cur_sum


                if abs(nums[j + 1] - target) <= abs(nums[k - 1] - target):
                    k -= 1
                else:
                    j += 1

        return closest


if __name__ == '__main__':

    nums = [4,0,5,-5,3,3,0,-4,-5]
    target = -2
    print(nums)
    result = Solution().threeSumClosest(nums, target)
    print(result)
