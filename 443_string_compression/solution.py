class Solution:
    def compress(self, chars: list[str]) -> int:
        
        cur_char = chars[0]
        cur_count = 1
        p = 0
        
        for i in range(1, len(chars)):
            if cur_char == chars[i]:
                cur_count += 1
            else:
                chars[p] = cur_char
                p += 1
                if (cur_count > 1):
                    for char in str(cur_count):
                        chars[p] = char
                        p += 1
                cur_count = 1
                cur_char = chars[i]

        chars[p] = cur_char
        p += 1
        if (cur_count > 1):
            for char in str(cur_count):
                chars[p] = char
                p += 1
        return p