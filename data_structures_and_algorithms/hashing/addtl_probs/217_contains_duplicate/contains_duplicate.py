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

    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/217_contains_duplicate/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.contains_duplicate(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
