import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given an array of integers temperatures represents the daily temperatures, return an array
        answer such that answer[i] is the number of days you have to wait after the ith day to get
        a warmer temperature. If there is no future day for which this is possible, keep
        answer[i] == 0 instead.

    Constraints:
        1 <= temperatures.length <= 10^5
        30 <= temperatures[i] <= 100

    """

    def daily_temperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/stacks_and_queues/addtl_probs/739_daily_temperatures/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: temperatures = {item['temperatures']}")
        output = solution.daily_temperatures(item["temperatures"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
