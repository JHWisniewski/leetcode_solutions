import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are given a 0-indexed array nums of n integers, and an integer k.

        The k-radius average for a subarray of nums centered at some index i with the radius k is
        the average of all elements in nums between the indices i - k and i + k (inclusive). If
        there are less than k elements before or after the index i, then the k-radius average
        is -1.

        Build and return an array avgs of length n where avgs[i] is the k-radius average for the
        subarray centered at index i.

        The average of x elements is the sum of the x elements divided by x, using integer
        division. The integer division truncates toward zero, which means losing its fractional
        part.

        For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4
        = 2.75, which truncates to 2.

    Constraints:
        n == nums.length
        1 <= n <= 10^5
        0 <= nums[i], k <= 10^5

    """

    def get_averages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prefix = [nums[0]]
        denom = 2 * k + 1
        ans = []

        # Build prefix
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        # Sliding window implementation with bound tests
        for i in range(len(nums)):
            left = i - k
            right = i + k

            if left < 0 or right >= len(nums):
                ans.append(-1)
            else:
                ans.append((prefix[right] - prefix[left] + nums[left]) // denom)

        return ans

    def get_averages_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i, total = 0, 0
        ans = []
        denom = 2 * k + 1

        # Sliding window implementation with bound tests
        # Step-by-step addition without use of a prefix
        while i < len(nums):
            left = i - k
            right = i + k

            if left < 0 or right >= len(nums):
                total += nums[i]
                ans.append(-1)
                i += 1
            elif i == k:
                for j in range(i, right + 1):
                    total += nums[j]
                ans.append(total // denom)
                total -= nums[left]
                i += 1
            else:
                total += nums[right]
                ans.append(total // denom)
                total -= nums[left]
                i += 1

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/7_k_radius_subarray_averages/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: nums = {item['nums']}, k = {item['k']}")
        output = solution.get_averages_2(item["nums"], item["k"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
