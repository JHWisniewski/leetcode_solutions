import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are given an array of integers nums, there is a sliding window of size k which is
        moving from the very left of the array to the very right. You can only see the k numbers in
        the window. Each time the sliding window moves right by one position.

        Return the max sliding window.

    Constraints:
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        1 <= k <= nums.length

    """

    def max_sliding_window(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque

        ans = []
        queue = deque()

        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            if queue[0] + k == i:
                queue.popleft()

            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/stacks_and_queues/addtl_probs/239_sliding_window_maximum/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: nums = {item['nums']}, k = {item['k']}")
        output = solution.max_sliding_window(item["nums"], item["k"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
