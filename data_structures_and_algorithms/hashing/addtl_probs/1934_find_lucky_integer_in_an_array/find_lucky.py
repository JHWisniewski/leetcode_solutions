import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an array of integers arr, a lucky integer is an integer that has a frequency in the
        array equal to its value.

        Return the largest lucky integer in the array. If there is no lucky integer return -1.

    Constraints:
        1 <= arr.length <= 500
        1 <= arr[i] <= 500

    """

    def find_lucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter

        count = Counter(arr)
        ans = -1

        for c in count:
            if count[c] == c:
                ans = max(ans, c)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/1934_find_lucky_integer_in_an_array/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: arr = {item['arr']}")
        output = solution.find_lucky(item["arr"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
