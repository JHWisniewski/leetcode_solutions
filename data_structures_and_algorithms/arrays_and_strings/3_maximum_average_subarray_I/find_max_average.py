import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are given an integer array nums consisting of n elements, and an integer k.

        Find a contiguous subarray whose length is equal to k that has the maximum average value
        and return this value. Any answer with a calculation error less than 10^-5 will be
        accepted.

    Constraints:
        n == nums.length
        1 <= k <= n <= 10^5
        -10^4 <= nums[i] <= 10^4

    """

    def find_max_average(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr, ans = 0, 0

        # Initial curr
        for i in range(k):
            curr += nums[i]

        # Store current average as ans
        ans = float(curr) / k

        # Calculate advancing curr with iterative calculations
        # Change window curr by adding new right bound (i) and subtracting old left bound (i - k)
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, float(curr) / k)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/3_maximum_average_subarray_I/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}, k = {item['k']}")
        output = solution.find_max_average(item["nums"], item["k"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
