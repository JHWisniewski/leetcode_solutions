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

        return s

#Setup of solution with LeetCode example input
solution = Solution()

input1 = ["h","e","l","l","o"]
input2 = ["H","a","n","n","a","h"]

print(f"Input: s = {input1}")
print(f"Output: " + str(solution.reverseString(input1)))
print()
print(f"Input: s = {input2}")
print(f"Output: " + str(solution.reverseString(input2)))