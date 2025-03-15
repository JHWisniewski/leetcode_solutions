import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.

        Your solution must use only constant extra space.

    Constraints:
        2 <= numbers.length <= 3 * 10^4
        -1000 <= numbers[i] <= 1000
        numbers is sorted in non-decreasing order.
        -1000 <= target <= 1000
        The tests are generated such that there is exactly one solution.

    """

    def two_sum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        from collections import defaultdict

        nums = defaultdict(int)

        for i, num in enumerate(numbers):
            nums[num] = i + 1

        for i, num in enumerate(numbers):
            if target - num in nums:
                return [i + 1, nums[target - num]]


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./miscellaneous/167_two_sum_II_input_array_is_sorted/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: numbers = {item['numbers']}, target = {item['target']}")
        output = solution.two_sum(item["numbers"], item["target"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
