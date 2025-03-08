import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given a binary tree root, a node X in the tree is named good if in the path from root to X
        there are no nodes with a value greater than X.

        Return the number of good nodes in the binary tree.

    Constraints:
        The number of nodes in the binary tree is in the range [1, 10^5].
        Each node's value is between [-10^4, 10^4].

    """

    def good_nodes(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans = 0
        stack = [(root, float("-inf"))]

        while stack:
            node, curr = stack.pop()
            if node.val >= curr:
                ans += 1

            if node.left:
                stack.append((node.left, max(curr, node.val)))

            if node.right:
                stack.append((node.right, max(curr, node.val)))

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/1448_count_good_nodes_in_binary_tree/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.good_nodes(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
