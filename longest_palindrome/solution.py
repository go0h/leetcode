class Solution:

    def is_palindrome(self, s: str, i: int, j: int):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        
        str_len = len(s)
        longest_pal_len = 0
        start, end = 0, 0

        i = 0
        while i < str_len and i + longest_pal_len < str_len:
            j = str_len - 1
            while i <= j and i + longest_pal_len <= j:
                if self.is_palindrome(s, i, j):
                    if j - i + 1 >= longest_pal_len:
                        longest_pal_len = j - i + 1
                        start, end = i, j + 1
                j -= 1
            i += 1
        
        return ''.join(s[start:end])

if __name__ == '__main__':
    s1 = 'a' 
    print(str(Solution().longestPalindrome(s1)))
