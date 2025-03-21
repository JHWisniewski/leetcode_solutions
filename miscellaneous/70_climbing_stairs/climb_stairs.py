import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the
        top?

    Constraints:
        1 <= n <= 45

    """

    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return -1


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./miscellaneous/70_climbing_stairs/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: n = {item['n']}")
        output = solution.climb_stairs(item["n"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
