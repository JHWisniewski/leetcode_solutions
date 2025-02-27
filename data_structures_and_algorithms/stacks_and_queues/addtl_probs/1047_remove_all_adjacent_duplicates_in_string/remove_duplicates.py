import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are given a string s consisting of lowercase English letters. A duplicate removal
        consists of choosing two adjacent and equal letters and removing them.

        We repeatedly make duplicate removals on s until we no longer can.

        Return the final string after all such duplicate removals have been made. It can be proven
        that the answer is unique.

    Constraints:
        1 <= s.length <= 10^5
        s consists of lowercase English letters.

    """

    def remove_duplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = ""

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return ans.join(stack)


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/stacks_and_queues/addtl_probs/1047_remove_all_adjacent_duplicates_in_string/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['s']}")
        output = solution.remove_duplicates(item["s"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
