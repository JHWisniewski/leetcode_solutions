import json

class Solution(object):
    """
    Description:
        A pangram is a sentence where every letter of the English alphabet appears at least once.

        Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

    Constraints:
        1 <= sentence.length <= 1000
        sentence consists of lowercase English letters.
        
    """
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        import string

        letters = set(string.ascii_lowercase)
        s_letters = set(sentence)

        return s_letters == letters

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/1_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: sentence = {object['sentence']}")
        output = solution.checkIfPangram(object['sentence'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()