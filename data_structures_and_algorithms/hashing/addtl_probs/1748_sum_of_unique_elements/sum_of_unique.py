import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one
        unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D
        plane and walk on the path specified by path.

        Return true if the path crosses itself at any point, that is, if at any time you are on a
        location you have previously visited. Return false otherwise.

    Constraints:
        1 <= path.length <= 10^4
        path[i] is either 'N', 'S', 'E', or 'W'.

    """

    def sum_of_unique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        ans = 0

        for num in nums:
            count[num] += 1

        for c in count:
            if count[c] == 1:
                ans += c

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/1748_sum_of_unique_elements/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.sum_of_unique(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
