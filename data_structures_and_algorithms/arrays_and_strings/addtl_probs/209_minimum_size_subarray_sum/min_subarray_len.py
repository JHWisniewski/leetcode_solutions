import json


class Solution(object):
    """
    Description:
        Given an array of positive integers nums and a positive integer target, return the minimal length of a
        subarray whose sum is greater than or equal to target.

        If there is no such subarray, return 0 instead.

    Constraints:
        1 <= target <= 10^9
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^4

    """

    def min_subarray_len(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, curr = 0, 0, 0

        # Set to minimum impossible value
        ans = len(nums) + 1

        # Run through nums
        while right < len(nums):
            curr += nums[right]

            if curr < target:
                right += 1
            else:
                while curr >= target:
                    ans = min(ans, right - left + 1)
                    curr -= nums[left]
                    left += 1

                right += 1

        # All feasible options exhausted
        if ans == len(nums) + 1:
            return 0

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/addtl_probs/209_minimum_size_subarray_sum/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: target = {item['target']}, nums = {item['nums']}")
        output = solution.min_subarray_len(item["target"], item["nums"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
