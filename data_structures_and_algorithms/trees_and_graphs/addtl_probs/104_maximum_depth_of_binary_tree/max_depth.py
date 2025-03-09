import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree, return its maximum depth.

        A binary tree's maximum depth is the number of nodes along the longest path from the root
        node down to the farthest leaf node.

    Constraints:
        The number of nodes in the tree is in the range [0, 10^4].
        -100 <= Node.val <= 100

    """

    def max_depth(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        stack = [(root, 1)]
        ans = 0

        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)

            if node.left:
                stack.append((node.left, depth + 1))

            if node.right:
                stack.append((node.right, depth + 1))

        return ans

    def max_depth_recursive(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return max(left, right) + 1


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/104_maximum_depth_of_binary_tree/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.max_depth(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
