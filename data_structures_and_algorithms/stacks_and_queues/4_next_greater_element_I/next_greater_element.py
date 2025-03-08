import json
from lib.test import test


class Solution(object):
    """
    Description:
        The next greater element of some element x in an array is the first greater element that is
        to the right of x in the same array.

        You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a
        subset of nums2.

        For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and
        determine the next greater element of nums2[j] in nums2. If there is no next greater
        element, then the answer for this query is -1.

        Return an array ans of length nums1.length such that ans[i] is the next greater element as
        described above.

    Constraints:
        1 <= nums1.length <= nums2.length <= 1000
        0 <= nums1[i], nums2[i] <= 10^4
        All integers in nums1 and nums2 are unique.
        All the integers of nums1 also appear in nums2.

    """

    def next_greater_element(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        hashmap = {}
        ans = []

        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num

            stack.append(num)

        while stack:
            hashmap[stack.pop()] = -1

        for num in nums1:
            ans.append(hashmap.get(num, -1))

        return ans

        # or
        # return [hashmap.get(num, -1) for num in nums1]


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/stacks_and_queues/4_next_greater_element_I/input.json"
    output = [None]

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums1 = {item['nums1']}, nums2 = {item['nums2']}")
        output = solution.next_greater_element(item["nums1"], item["nums2"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
