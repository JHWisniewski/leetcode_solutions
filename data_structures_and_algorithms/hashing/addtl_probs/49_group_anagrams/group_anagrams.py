import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an array of strings strs, group the anagrams together.
        You can return the answer in any order.

    Constraints:
        1 <= strs.length <= 10^4
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.

    """

    def group_anagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        groups = defaultdict(list)

        for s in strs:
            word = "".join(sorted(s))
            groups[word].append(s)

        return list(groups.values())


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/49_group_anagrams/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: strs = {item['strs']}")
        output = solution.group_anagrams(item["strs"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        print("Output sorted by LeetCode, ensure groups in each Output are equal.")
        print()


if __name__ == "__main__":
    main()
