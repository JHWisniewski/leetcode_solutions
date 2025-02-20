import json
from lib.reverse_string import reverse_string

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
    def reverse_words(self, s):
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
                string[left:right] = reverse_string(string[left:right])
                right += 1
                left = right
            elif right == len(s) - 1:
                string[left:right + 1] = reverse_string(string[left:right + 1])
                right += 1
            else:
                right += 1

        #Convert list to str
        ans = ''.join(string)

        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    path = './data_structures_and_algorithms/arrays_and_strings/addtl_probs/557_reverse_words_in_a_string_III/input.json'

    with open(path, encoding = "utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['s']}")
        output = solution.reverse_words(item['s'])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
