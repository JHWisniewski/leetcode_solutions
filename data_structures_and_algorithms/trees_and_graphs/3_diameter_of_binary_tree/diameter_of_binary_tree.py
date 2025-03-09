import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree, return the length of the diameter of the tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a
        tree. This path may or may not pass through the root.

        The length of a path between two nodes is represented by the number of edges between them.

    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        -100 <= Node.val <= 100

    """

    def diameter_of_binary_tree(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diameter = 0

        def longest_path(node: TreeNode):
            if not node:
                return 0
            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/3_diameter_of_binary_tree/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.diameter_of_binary_tree(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
