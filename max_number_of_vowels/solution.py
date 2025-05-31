class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
        
        cur_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                vowels[s[i]] += 1
                cur_vowels += 1

        max_vowels = cur_vowels

        for i in range(k, len(s)):

            if max_vowels == k:
                return max_vowels

            if s[i] in vowels:
                cur_vowels += 1
            if s[i - k] in vowels:
                cur_vowels -= 1

            max_vowels = max(max_vowels, cur_vowels)

        return max_vowels


if __name__ == '__main__':

    s = "abciiidef"
    k = 3
    result = Solution().maxVowels(s, k)
    print(result)