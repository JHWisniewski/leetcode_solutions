import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a binary array nums and an integer k, return the maximum number of consecutive
        1's in the array if you can flip at most k 0's.

    Constraints:
        1 <= nums.length <= 10^5
        nums[i] is either 0 or 1.
        0 <= k <= nums.length

    """

    def longest_ones(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, curr, ans = 0, 0, 0

        for right, num in enumerate(nums):
            if num == 0:
                curr += 1

            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/4_max_consecutive_ones_III/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}, k = {item['k']}")
        output = solution.longest_ones(item["nums"], item["k"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
