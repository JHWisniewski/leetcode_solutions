import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an array of integers nums and an integer k, return the total number
        of subarrays whose sum equals to k.

        A subarray is a contiguous non-empty sequence of elements within an array.

    Constraints:
        1 <= nums.length <= 2 * 10^4
        -1000 <= nums[i] <= 1000
        -10^7 <= k <= 10^7

    """

    def subarray_sum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        counts = defaultdict(int)
        curr, ans = 0, 0
        counts[0] = 1

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/560_subarray_sum_equals_k/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}, k = {item['k']}")
        output = solution.subarray_sum(item["nums"], item["k"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
