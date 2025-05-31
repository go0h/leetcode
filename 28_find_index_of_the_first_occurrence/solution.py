class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while i < len(haystack) - len(needle):

            if haystack[i] == needle[0]:
                j = i
                k = 0
                while k < len(needle) and j < len(haystack):
                    if needle[k] != haystack[k]:
                        break
                    j += 1
                    k += 1

                if j - i == len(needle):
                    return i
            i += 1

        return -1
