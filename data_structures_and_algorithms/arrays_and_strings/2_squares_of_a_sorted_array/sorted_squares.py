import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an integer array nums sorted in non-decreasing order, return an array
        of the squares of each number sorted in non-decreasing order.

    Constraints:
        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        nums is sorted in non-decreasing order.

    """

    def sorted_squares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Square each element
        for i, num in enumerate(nums):
            nums[i] = num**2

        # Base cases
        if len(nums) == 0 or len(nums) == 1:
            return nums

        # Two pointers for sorting into ans
        i = 0
        j = len(nums) - 1

        # Pre-allocate ans array space and set pos index for backwards interation
        # Avoids needing to reverse appended array
        ans = [0] * len(nums)
        pos = len(nums) - 1

        while i <= j:
            if nums[i] >= nums[j]:
                ans[pos] = nums[i]
                i += 1
            else:
                ans[pos] = nums[j]
                j -= 1
            pos -= 1

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/2_squares_of_a_sorted_array/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.sorted_squares(item["nums"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
