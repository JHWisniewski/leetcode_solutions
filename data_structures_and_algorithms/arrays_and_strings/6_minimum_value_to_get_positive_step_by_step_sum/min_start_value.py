import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an array of integers nums, you start with an initial positive value startValue.

        In each iteration, you calculate the step by step sum of startValue plus elements
        in nums (from left to right).

        Return the minimum positive value of startValue such that the step by step sum is
        never less than 1.

    Constraints:
        1 <= nums.length <= 100
        -100 <= nums[i] <= 100

    """

    # Brute force, O(n^2)
    def min_start_value_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        start_val = 1
        prefix = [start_val]

        while i < len(nums):
            if nums[i] + prefix[-1] > 0:
                prefix.append(nums[i] + prefix[-1])
                i += 1
            else:
                start_val += 1
                i = 0
                prefix = [start_val]

        return start_val

    # O(n) solution
    def min_start_value_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_val, total = 0, 0

        # Keep just step-by-step calculation in mind
        # All we need is the minium step value
        for num in nums:
            total += num
            start_val = min(start_val, total)

        return -start_val + 1


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/6_minimum_value_to_get_positive_step_by_step_sum/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.min_start_value_2(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
