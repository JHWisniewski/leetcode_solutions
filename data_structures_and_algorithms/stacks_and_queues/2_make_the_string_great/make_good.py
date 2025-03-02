import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a string s of lower and upper case English letters.

        A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1]
        where:

        0 <= i <= s.length - 2
        s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or
        vice-versa.

        To make the string good, you can choose two adjacent characters that make the string bad
        and remove them. You can keep doing this until the string becomes good.

        Return the string after making it good. The answer is guaranteed to be unique under the
        given constraints.

        Notice that an empty string is also good.

    Constraints:
        1 <= s.length <= 100
        s contains only lower and upper case English letters.

    """

    def make_good(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if stack and stack[-1] == stack[-1].lower() and c == stack[-1].upper():
                stack.pop()
            elif (
                stack
                and stack
                and stack[-1] == stack[-1].upper()
                and c == stack[-1].lower()
            ):
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/stacks_and_queues/2_make_the_string_great/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['s']}")
        output = solution.make_good(item["s"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
