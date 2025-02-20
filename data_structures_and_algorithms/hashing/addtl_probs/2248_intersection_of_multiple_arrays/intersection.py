import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a 2D integer array nums where nums[i] is a non-empty array of
        distinct positive integers, return the list of integers that are
        present in each array of nums sorted in ascending order.

    Constraints:
        1 <= nums.length <= 1000
        1 <= sum(nums[i].length) <= 1000
        1 <= nums[i][j] <= 1000
        All the values of nums[i] are unique.

    """

    def iterative_intersection(self, nums):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        res = []

        for arr in nums:
            for el in arr:
                count[el] += 1

        for num in count:
            if count[num] == len(nums):
                res.append(num)

        return sorted(res)

    def operator_intersection(self, nums):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 1 <= nums.length <= 1000
        intersection = set(nums[0])

        for i in range(1, len(nums)):
            intersection &= set(nums[i])

        return sorted(list(intersection))


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/2248_intersection_of_multiple_arrays/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}")
        output = solution.operator_intersection(item["nums"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
