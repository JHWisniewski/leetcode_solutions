import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root node of a binary search tree and two integers low and high, return the sum
        of values of all nodes with a value in the inclusive range [low, high].

    Constraints:
        The number of nodes in the tree is in the range [1, 2 * 10^4].
        1 <= Node.val <= 10^5
        1 <= low <= high <= 10^5
        All Node.val are unique.

    """

    def range_sum_bst(self, root: TreeNode, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        stack = [(root)]
        ans = 0

        while stack:
            node = stack.pop()

            if low <= node.val and node.val <= high:
                ans += node.val

            if node.left and low < node.val:
                stack.append(node.left)

            if node.right and high > node.val:
                stack.append(node.right)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/938_range_sum_of_bst/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(
            f"Input: root = {item['root']}, low = {item['low']}, high = {item['high']}"
        )
        output = solution.range_sum_bst(
            binary_tree(item["root"]), item["low"], item["high"]
        )
        test(output, item["expected"])


if __name__ == "__main__":
    main()
