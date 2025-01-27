import json

class Solution(object):
    """
    Constraints:
        1 <= s.length <= 10^5
        s[i] is a printable ascii character.
    """
    
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #Two pointers for reversing string
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
            left += 1
            right -= 1

        return s

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/1_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: s = {object['s']}")
        output = solution.reverseString(object['s'])
        print(f"Output: {output}\n")

if __name__ == "__main__":
    main()