class Solution:

    def findAnagrams(self, s: str, p: str) -> list[int]:

        def is_anagram(dict_chars_in_slice, dict_p):
            for key in dict_p.keys():
                if dict_chars_in_slice[key] != dict_p[key]:
                    return False
            return True

        result = []

        dict_p = dict()
        for i in range(len(p)):
            dict_p[p[i]] = dict_p.get(p[i]) + 1

        dict_chars_in_slice = dict([(chr(97 + i), 0) for i in range(26)])
        i = 0
        while i < len(s) and i < len(p):
            dict_chars_in_slice[s[i]] += 1
            i += 1

        left = 0
        right = len(p) - 1

        while right < len(s) - 1:
            
            if is_anagram(dict_chars_in_slice, dict_p):
                result.append(left)

            dict_chars_in_slice[s[left]] -= 1
            left += 1

            right += 1
            dict_chars_in_slice[s[right]] += 1

        if is_anagram(dict_chars_in_slice, dict_p):
            result.append(left)

        return result
    
if __name__ == '__main__':

    p = "aaaaaaaaaaaaa"
    s = "aaaaaaaaaaa"
    res = Solution().findAnagrams(s, p)

    print(res)