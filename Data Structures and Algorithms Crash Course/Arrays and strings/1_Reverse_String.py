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

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/1_Input.md') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        s = eval(line)
        output = solution.reverseString(s)
        
        #s is changed in place, line itself used
        print(f"Input: s = {line}")

        print(f"Output: {output}\n")  

if __name__ == "__main__":
    main()