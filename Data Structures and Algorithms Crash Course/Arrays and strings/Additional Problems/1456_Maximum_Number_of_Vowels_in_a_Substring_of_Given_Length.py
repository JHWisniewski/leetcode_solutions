import json

class Solution(object):
    """
    Description:
        Given a string s and an integer k, return the maximum number of vowel letters in any substring
        of s with length k.

        Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

    Constraints:
        1 <= s.length <= 10^5
        s consists of lowercase English letters.
        1 <= k <= s.length

    """
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = k - 1
        curr, ans = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        #Initial substring build
        while left <= right:
            if s[left] in vowels:
                curr += 1
                ans = max(ans, curr)
                left += 1
            else:
                left += 1

        #Setup window expansion and shrink
        left = 0
        right += 1

        #Rest of substrings
        while right < len(s):
            if s[right] in vowels:
                curr += 1
            if s[left] in vowels:
                curr -= 1
            ans = max(ans, curr)
            left += 1
            right += 1

        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()

    with open('./Problem Inputs/1456_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: s = {object['s']}, k = {object['k']}")
        output = solution.maxVowels(object['s'], object['k'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
        