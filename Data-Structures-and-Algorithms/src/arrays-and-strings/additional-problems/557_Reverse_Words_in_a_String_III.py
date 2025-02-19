import json
from lib.reverseString import reverseString

class Solution(object):
    """
    Description:
        Given a string s, reverse the order of characters in each word within a 
        sentence while still preserving whitespace and initial word order.
        
    Constraints:
        1 <= s.length <= 5 * 10^4
        s contains printable ASCII characters.
        s does not contain any leading or trailing spaces.
        There is at least one word in s.
        All the words in s are separated by a single space.
        
    """
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0

        #Convert immutable str s to list string
        string = list(s)

        #Identify words and pass them into reverseString function
        while right < len(s):
            if s[right] == ' ':
                string[left:right] = reverseString(string[left:right])
                right += 1
                left = right
            elif right == len(s) - 1:
                string[left:right + 1] = reverseString(string[left:right + 1])
                right += 1
            else:
                right += 1

        #Convert list to str
        ans = ''.join(string)
        
        return ans
        
def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Data-Structures-and-Algorithms/data/arrays-and-strings/557_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: s = {object['s']}")
        output = solution.reverseWords(object['s'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()