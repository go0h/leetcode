class Solution:
        
    # def lengthOfLongestSubstring(self, s: str) -> int:
        
    #     str_len = len(s)
    #     longest_subst = 0

    #     unique_vals = set()

    #     for i in range(str_len):
    #         for j in range(i, str_len):
    #             if s[j] not in unique_vals:
    #                 unique_vals.add(s[j])
    #             else:
    #                 longest_subst = max(longest_subst, len(unique_vals))
    #                 unique_vals = set()
    #                 break
        
    #     return max(longest_subst, len(unique_vals))

    def lengthOfLongestSubstring(self, s: str) -> int:

        str_len = len(s)
        longest_subst = 0

        unique_vals = []

        j = 0
        while j < str_len:
            
            if s[j] not in unique_vals:
                unique_vals.append(s[j])
            else:
                longest_subst = max(longest_subst, len(unique_vals))

                i = 0
                while unique_vals.pop(0) != s[j]:
                    i += 1

                unique_vals.append(s[j])
            j += 1
        
        return max(longest_subst, len(unique_vals))



if __name__ == '__main__':
    s1 = 'dvdf' 
    print(str(Solution().lengthOfLongestSubstring(s1)))
