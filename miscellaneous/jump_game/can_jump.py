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

    def can_jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = [nums[0]]
        index = 0

        while stack:
            if index + stack[-1] >= len(nums) - 1:
                return True
            else:
                stack.append(nums[index + stack.pop()])
                index += 1

        return False


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./miscellaneous/jump_game/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.can_jump(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
