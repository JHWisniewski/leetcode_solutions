import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that
        row ri and column cj are equal.

        A row and column pair is considered equal if they contain the same elements in the same
        order (i.e., an equal array).

    Constraints:
        n == grid.length == grid[i].length
        1 <= n <= 200
        1 <= grid[i][j] <= 10^5

    """

    def equal_pairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        ans = 0

        for row in grid:
            count[tuple(row)] += 1

        cols = [
            [grid[row][col] for row in range(len(grid))] for col in range(len(grid))
        ]

        """
        # For general traversal of 2d arrays
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] ---> traverse rows
                grid[j][i] ---> traverse cols
        """

        for col in cols:
            ans += count[tuple(col)]

        return ans

    def equal_pairs_leetcode(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import Counter

        c = Counter()
        ans = 0

        for row in grid:
            c[tuple(row)] += 1

        # Stupid python magic with zip function and * expander
        # Not useful for explanation in interview, but * looks cool for later
        for col in zip(*grid):
            if col in c:
                ans += c[col]

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/2352_equal_row_and_column_pairs/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: grid = {item['grid']}")
        output = solution.equal_pairs(item["grid"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
