import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an integer array nums, return the largest integer that only occurs once.

        If no integer occurs once, return -1.

    Constraints:
        1 <= nums.length <= 2000
        0 <= nums[i] <= 1000

    """

    def largest_unique_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        once = []

        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            if freq == 1:
                once.append(num)

        if once:
            return max(once)

        return -1


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/5_largets_unique_number/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.largest_unique_number(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
