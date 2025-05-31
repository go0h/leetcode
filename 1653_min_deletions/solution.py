# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         stack_a = [0] * len(s)
#         stack_b = [0] * len(s)
        
#         sum_a = 0
#         sum_b = 0
#         idx_a = 0
#         idx_b = len(s) - 1
#         while idx_a < len(s) and idx_b > -1:

#             stack_a[idx_a] = sum_a
#             stack_b[idx_b] = sum_b
            
#             if s[idx_a] == 'b':
#                 sum_a += 1

#             if s[idx_b] == 'a':
#                 sum_b += 1

#             idx_a += 1
#             idx_b -= 1

#         mid_dels = len(s)
#         for i in range(len(s)):
#             mid_dels = min(mid_dels, stack_a[i] + stack_b[i])

#         return mid_dels

class Solution:
    def minimumDeletions(self, s: str) -> int:
        sum_deletes = [0] * len(s)
        
        sum_a = 0
        sum_b = 0
        idx_a = 0
        idx_b = len(s) - 1
        while idx_a < len(s) and idx_b > -1:

            sum_deletes[idx_a] += sum_a
            sum_deletes[idx_b] += sum_b
            
            if s[idx_a] == 'b':
                sum_a += 1

            if s[idx_b] == 'a':
                sum_b += 1

            idx_a += 1
            idx_b -= 1

        return min(sum_deletes)

if __name__ == '__main__':

    s = "baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb"
    # s = "a"
    # s = "b"
    # s = "aababbab"
    # s = "bbaaaaabb"
    print(s)
    result = Solution().minimumDeletions(s)
    print(result)