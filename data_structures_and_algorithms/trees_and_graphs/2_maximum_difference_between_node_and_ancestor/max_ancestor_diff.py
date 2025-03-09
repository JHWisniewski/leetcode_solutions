import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree, find the maximum value v for which there exist different
        nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

        A node a is an ancestor of b if either: any child of a is equal to b or any child of a is
        an ancestor of b.

        Note: A leaf is a node with no children.

    Constraints:
        The number of nodes in the tree is in the range [2, 5000].
        0 <= Node.val <= 10^5

    """

    def max_ancestor_diff(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def helper(node: TreeNode, cur_max, cur_min):
            if not node:
                return cur_max - cur_min

            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)

            return max(left, right)

        return helper(root, root.val, root.val)


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/2_maximum_difference_between_node_and_ancestor/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.max_ancestor_diff(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
