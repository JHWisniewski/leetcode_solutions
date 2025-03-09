import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are given an array nums consisting of positive integers.

        Return the total frequencies of elements in nums such that those elements all have the
        maximum frequency.

        The frequency of an element is the number of occurrences of that element in the array.

    Constraints:
        1 <= nums.length <= 100
        1 <= nums[i] <= 100

    """

    def max_frequency_elements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        max_freq, ans = 0, 0

        for num in nums:
            count[num] += 1
            max_freq = max(max_freq, count[num])

        for c in count:
            if count[c] == max_freq:
                ans += max_freq

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/3005_count_elements_with_maximum_frequency/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.max_frequency_elements(item["nums"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
