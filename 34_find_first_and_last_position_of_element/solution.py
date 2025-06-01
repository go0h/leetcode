class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result[0] = mid
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result[1] = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return result

if __name__ == '__main__':

    nums = [5,7,7,8,10]
    target = 8

    result = Solution().searchRange(nums, target)
    print(result)
