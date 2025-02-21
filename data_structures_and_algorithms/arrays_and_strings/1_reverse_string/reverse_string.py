import json
from lib.test import test


class Solution(object):
    """
    Description:
        Write a function that reverses a string. The input string is given as an array of
        characters s.

        You must do this by modifying the input array in-place with O(1) extra memory.

    Constraints:
        1 <= s.length <= 10^5
        s[i] is a printable ascii character.

    """

    def reverse_string(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Two pointers for reversing string
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
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/1_reverse_string/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['s']}")
        output = solution.reverse_string(item["s"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
