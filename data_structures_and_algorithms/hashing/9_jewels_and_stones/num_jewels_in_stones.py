import json
from lib.test import test


class Solution(object):
    """
    Description:
        You're given strings jewels representing the types of stones that are jewels, and stones
        representing the stones you have. Each character in stones is a type of stone you have.
        You want to know how many of the stones you have are also jewels.

        Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Constraints:
        1 <= jewels.length, stones.length <= 50
        jewels and stones consist of only English letters.
        All the characters of jewels are unique.

    """

    def num_jewels_in_stones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        from collections import Counter

        stone_count = Counter(stones)
        count = 0

        for jewel in jewels:
            if jewel in stone_count:
                count += stone_count[jewel]

        return count


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/9_jewels_and_stones/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: jewels = {item['jewels']}, stones = {item['stones']}")
        output = solution.num_jewels_in_stones(item["jewels"], item["stones"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
