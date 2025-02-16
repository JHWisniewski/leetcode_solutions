import json

class Solution(object):
    """
    Description:
        Given a string text, you want to use the characters of text to form as many instances 
        of the word "balloon" as possible.

        You can use each character in text at most once. Return the maximum number of 
        instances that can be formed.

    Constraints:
        1 <= text.length <= 10^4
        text consists of lower case English letters only.
        
    """
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import defaultdict

        balloon = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        
        count = defaultdict(int)
        instances = []

        for letter in text:
            if letter in balloon:
                count[letter] += 1

        for letter in balloon:
            if count[letter] == 0:
                return 0
            else:
                instances.append(count[letter] // balloon[letter])

        return min(instances)

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/6_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: text = {object['text']}")
        output = solution.maxNumberOfBalloons(object['text'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()