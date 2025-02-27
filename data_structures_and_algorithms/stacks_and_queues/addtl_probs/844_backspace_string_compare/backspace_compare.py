import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given two strings s and t, return true if they are equal when both are typed into empty
        text editors. '#' means a backspace character.

        Note that after backspacing an empty text, the text will continue empty.

    Constraints:
        1 <= s.length, t.length <= 200
        s and t only contain lowercase letters and '#' characters.

    """

    def backspace_compare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_stack = []
        t_stack = []

        for c in s:
            if s_stack and c == "#":
                s_stack.pop()
            elif c != "#":
                s_stack.append(c)

        for c in t:
            if t_stack and c == "#":
                t_stack.pop()
            elif c != "#":
                t_stack.append(c)

        return s_stack == t_stack


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/stacks_and_queues/addtl_probs/844_backspace_string_compare/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['s']}, t = {item['t']}")
        output = solution.backspace_compare(item["s"], item["t"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
