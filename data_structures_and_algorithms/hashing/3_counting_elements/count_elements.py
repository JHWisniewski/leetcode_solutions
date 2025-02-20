import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an integer array arr, count how many elements x there are, such that x + 1 is also
        in arr.

        If there are duplicates in arr, count them separately.

    Constraints:
        1 <= arr.length <= 1000
        0 <= arr[i] <= 1000

    """

    def count_elements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter

        nums = Counter(arr)
        ans = 0

        for num in nums:
            if num + 1 in nums:
                ans += nums[num]

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/3_counting_elements/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: arr = {item['arr']}")
        output = solution.count_elements(item["arr"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
