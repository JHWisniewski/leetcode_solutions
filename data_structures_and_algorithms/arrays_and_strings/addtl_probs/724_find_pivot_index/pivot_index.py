import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an array of integers nums, calculate the pivot index of this array.

        The pivot index is the index where the sum of all the numbers strictly to the left of the
        index is equal to the sum of all the numbers strictly to the index's right.

        If the index is on the left edge of the array, then the left sum is 0 because there are no
        elements to the left. This also applies to the right edge of the array.

        Return the leftmost pivot index. If no such index exists, return -1.

    Constraints:
        1 <= nums.length <= 10^4
        -1000 <= nums[i] <= 1000

    """

    def pivot_index(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, l_sum, r_sum = 0, 0, 0
        prefix = [nums[0]]

        # Build prefix
        # No other solution without this as far as I can tell
        for j in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[j])

        # Iterate through and compare left sum to right sum
        while i < len(nums):
            l_sum = prefix[i]
            r_sum = prefix[-1] - prefix[i] + nums[i]

            if l_sum == r_sum:
                return i

            i += 1

        return -1


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/addtl_probs/724_find_pivot_index/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.pivot_index(item["nums"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
