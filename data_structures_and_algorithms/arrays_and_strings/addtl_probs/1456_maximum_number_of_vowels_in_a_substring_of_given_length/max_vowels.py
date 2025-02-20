import json
from lib.test import test


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

    def max_vowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = k - 1
        curr, ans = 0, 0
        vowels = {"a", "e", "i", "o", "u"}

        # Initial substring build
        while left <= right:
            if s[left] in vowels:
                curr += 1
                ans = max(ans, curr)
                left += 1
            else:
                left += 1

        # Setup window expansion and shrink
        left = 0
        right += 1

        # Rest of substrings
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
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/addtl_probs/1456_maximum_number_of_vowels_in_a_substring_of_given_length/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['s']}, k = {item['k']}")
        output = solution.max_vowels(item["s"], item["k"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
