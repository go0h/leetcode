class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        
        max_seq = 1
        cur_seq = 1
        prev_val = nums[0]
        for i in range(1, len(nums)):
            print(f"{prev_val}, {nums[i]}")
            if prev_val != nums[i]:
                max_seq = max(max_seq, cur_seq)
                cur_seq = 1
            else:
                cur_seq += 1
            prev_val = nums[i]
            print(str(max_seq))
        return max(cur_seq, max_seq)

if __name__ == '__main__':

    print(str(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])))
