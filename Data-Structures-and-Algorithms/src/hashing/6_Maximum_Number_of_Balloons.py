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
        from collections import Counter

        balloon = Counter('balloon')
        count = defaultdict(int)

        for letter in text:
            if letter in balloon:
                count[letter] += 1

        for letter in balloon:
            if count[letter] == 0:
                return 0
            else:
                count[letter] //= balloon[letter]

        return min(count.values())

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Data-Structures-and-Algorithms/data/hashing/6_Input.json') as f:
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