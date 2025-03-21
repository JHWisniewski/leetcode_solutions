import json
from lib.misc import sum_digits
from lib.test import test


class Solution(object):
    """
    Description:
        You are given a 0-indexed array nums consisting of positive integers.
        You can choose two indices i and j, such that i != j, and the sum of
        digits of the number nums[i] is equal to that of nums[j].

        Return the maximum value of nums[i] + nums[j] that you can obtain
        over all possible indices i and j that satisfy the conditions. If no
        such pair of indices exists, return -1.

    Constraints:
        1 <= nums.length <= 10^5
        0 <= nums[i] <= 10^9

    """

    def maximum_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        curr = 0
        ans = -1

        for num in nums:
            curr = sum_digits(num)

            if curr in counts:
                ans = max(ans, counts[curr] + num)
                counts[curr] = max(counts[curr], num)
            else:
                counts[curr] = num

            curr = 0

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/2342_max_sum_of_a_pair_with_equal_sum_of_digits/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.maximum_sum(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
