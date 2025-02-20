import json


class Solution(object):
    """
    Description:
        Given an array nums. We define a running sum of an array
        as runningSum[i] = sum(nums[0]…nums[i]).

        Return the running sum of nums.

    Constraints:
        1 <= nums.length <= 1000
        -10^6 <= nums[i] <= 10^6

    """

    def running_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        return prefix


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/5_running_sum_of_1d_array/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: s = {item['nums']}")
        output = solution.running_sum(item["nums"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
