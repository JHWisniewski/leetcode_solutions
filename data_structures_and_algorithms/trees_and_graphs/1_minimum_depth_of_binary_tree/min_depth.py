import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given a binary tree, find its minimum depth.

        The minimum depth is the number of nodes along the shortest path from the root node down to
        the nearest leaf node.

        Note: A leaf is a node with no children.

    Constraints:
        The number of nodes in the tree is in the range [0, 10^5].
        -1000 <= Node.val <= 1000

    """

    def min_depth(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        stack = [(root, 0)]
        ans = float("inf")

        while stack:
            node, depth = stack.pop()

            if not node.left and not node.right:
                ans = min(ans, depth + 1)

            if node.left:
                stack.append((node.left, depth + 1))

            if node.right:
                stack.append((node.right, depth + 1))

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/1_minimum_depth_of_binary_tree/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.min_depth(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
