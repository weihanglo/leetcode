# Question: https://leetcode.com/problems/implement-strstr/
#
# Implement strStr(). http://www.cplusplus.com/reference/cstring/strstr/
# 
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# 
# Example 1:
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# Example 2:
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# str.find


# Regular expression
import re
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        res = re.search(needle, haystack)
        if not res:
            return -1
        return res.span()[0]

# str.find
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack.find(needle)

# Linear search
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        if not length:
            return 0
        for i, c in enumerate(haystack):
            if c == needle[0] and haystack[i:i+length] == needle:
                return i
        return -1
