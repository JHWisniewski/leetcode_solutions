import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an array of positive integers nums and a positive integer target, return the minimal length of a
        subarray whose sum is greater than or equal to target.

        If there is no such subarray, return 0 instead.

    Constraints:
        1 <= target <= 10^9
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^4

    """

    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0

        for right in range(len(nums)):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left] != 0:
                left += 1

        return nums

    def move_zeroes_bad(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        from collections import deque

        queue = deque()
        stack = []

        for num in nums:
            if num != 0:
                queue.append(num)
            else:
                stack.append(num)

        for i in range(len(nums)):
            if queue:
                nums[i] = queue.popleft()
            else:
                nums[i] = stack.pop()

        return nums


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/addtl_probs/283_move_zeroes/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.move_zeroes(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
