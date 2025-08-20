class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_list = []
        max_len = 0

        for i in range(len(s)):
            if s[i] in new_list:
                dup_index = new_list.index(s[i])
                del new_list[0:dup_index+1]
            
            new_list.append(s[i])
            max_len = max(max_len, len(new_list))

        return(max_len)
            
