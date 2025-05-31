class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        char_count = dict()
        max_repeated_char = 0

        for right in range(len(s)):
            
            if s[right] in char_count:
                char_count[s[right]] += 1
                max_repeated_char = max(char_count[s[right]], max_repeated_char)
            else:
                char_count[s[right]] = 1
                max_repeated_char = max(char_count[s[right]], max_repeated_char)

            if (right - left + 1) - max_repeated_char <= k:
                max_length = max(max_length, right - left + 1)
            else:
                if char_count[s[left]] == max_repeated_char:
                    max_repeated_char -= 1
                char_count[s[left]] -= 1
                left += 1
        
        return max_length
    
if __name__ == '__main__':

    s = "ABAB"
    k = 2
    res = Solution().characterReplacement(s, k)

    print(res)