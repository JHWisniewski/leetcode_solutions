import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.

    Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9

    """

    def is_isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return 0


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/205_isomorphic_strings/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['s']}, t = {item['t']}")
        output = solution.is_isomorphic(item["s"], item["t"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
