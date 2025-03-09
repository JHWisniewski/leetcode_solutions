import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine
        if the input string is valid.

        An input string is valid if:

        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.

    Constraints:
        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.

    """

    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False

                left = stack.pop()

                if matching[left] != c:
                    return False

        if stack:
            return False
        return True


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/stacks_and_queues/addtl_probs/20_valid_parentheses/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: s = {item['s']}")
        output = solution.is_valid(item["s"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
