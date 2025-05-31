class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        i = 0
        j = len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        return ' '.join([word.strip() for word in arr if word != ''])
        

if __name__ == '__main__':

    s = "the sky is blue"
    print(s)
    result = Solution().reverseWords(s)
    print(result)