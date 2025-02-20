import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a binary array nums, return the maximum length of a
        contiguous subarray with an equal number of 0 and 1.

    Constraints:
        1 <= nums.length <= 10^5
        nums[i] is either 0 or 1.

    """

    def find_max_length(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        counts = defaultdict(int)
        curr, ans = 0, 0
        counts[0] = -1

        for i, num in enumerate(nums):
            curr += 1 if num == 1 else -1

            if curr in counts:
                ans = max(ans, i - counts[curr])
            else:
                counts[curr] = i

        return ans

    def find_max_length_hard(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        diff, ans = 0, 0
        diff_ind = defaultdict(int)

        for i, num in enumerate(nums):
            if num == 0:
                diff += 1
            else:
                diff -= 1

            if diff not in diff_ind:
                diff_ind[diff] = i

            if diff == 0:
                ans = i + 1
            else:
                ans = max(ans, i - diff_ind[diff])

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/7_contiguous_array/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.find_max_length(item["nums"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")
        test(output, item["expected"])


if __name__ == "__main__":
    main()
