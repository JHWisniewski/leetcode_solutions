import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are given an integer array nums. The unique elements of an array are the elements that
        appear exactly once in the array.

        Return the sum of all the unique elements of nums.

    Constraints:
        1 <= nums.length <= 100
        1 <= nums[i] <= 100

    """

    def sum_of_unique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        count = Counter(nums)
        ans = 0

        for c in count:
            if count[c] == 1:
                ans += c

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/1748_sum_of_unique_elements/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.sum_of_unique(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
