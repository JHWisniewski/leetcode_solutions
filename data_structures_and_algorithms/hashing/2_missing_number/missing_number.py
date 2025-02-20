import json


class Solution(object):
    """
    Description:
        Given an array nums containing n distinct numbers in the range [0, n], return the only
        number in the range that is missing from the array.

    Constraints:
        n == nums.length
        1 <= n <= 10^4
        0 <= nums[i] <= n
        All the numbers of nums are unique.

    """

    def missing_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)

        for i in range(len(nums) + 1):
            if i not in nums:
                return i


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/2_missing_number/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.missing_number(item["nums"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
