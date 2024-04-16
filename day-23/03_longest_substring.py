# 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map ={}
        start = 0
        max_length = start

        for i ,char in enumerate(s):

            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char]+1

            else:
                max_length = max(max_length,i-start+1)

            char_index_map[char] = i

        return max_length


                
        
s='pwwkew'
substring = Solution()
x = substring.lengthOfLongestSubstring(s)

print(x)