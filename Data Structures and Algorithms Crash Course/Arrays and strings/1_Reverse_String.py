class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #Two pointers for reversing string
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
            i += 1
            j -= 1