import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a string s, find the length of the longest substring without duplicate characters.

    Constraints:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.

    """

    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        left, ans = 0, 0

        for right, letter in enumerate(s):
            count[letter] += 1

            while count[letter] > 1:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/10_longest_substring_without_repeating_characters/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['s']}")
        output = solution.length_of_longest_substring(item["s"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
