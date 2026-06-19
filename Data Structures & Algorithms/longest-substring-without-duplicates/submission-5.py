class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        saved = [0]
        letters = []
        for right in range(len(s)):

            while s[right] in letters:
                left+=1
                letters.pop(0)
            no_to_save = (right+1) - left
            saved.append(no_to_save)

            letters.append(s[right])    

        max_num = max(saved)
        return max_num

        