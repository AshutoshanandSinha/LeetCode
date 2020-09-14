class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = left = right = 0
        chars = set()
        while left < len(s) and right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                maxlength = max(maxlength, right - left)
            else:
                chars.remove(s[left])
                left += 1
        return maxlength

if __name__ == '__main__':
    sol1 = Solution()

    word = "abcabcbb"

    assert 2 == sol1.lengthOfLongestSubstring(word)

