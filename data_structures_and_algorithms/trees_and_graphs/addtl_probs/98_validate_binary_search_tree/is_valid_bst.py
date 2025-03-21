import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).

        A valid BST is defined as follows:

            The left subtree of a node contains only nodes with keys less than the node's key.
            The right subtree of a node contains only nodes with keys greater than the node's key.
            Both the left and right subtrees must also be binary search trees.

    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        -2^31 <= Node.val <= 2^31 - 1

    """

    def is_valid_bst(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack = []
        vals = []
        curr = root

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                vals.append(curr.val)
                curr = curr.right

        # The number of nodes in the tree is in the range [1, 10^4].
        for i in range(1, len(vals)):
            if vals[i] == vals[i - 1] or vals[i] < vals[i - 1]:
                return False

        return True


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/98_validate_binary_search_tree/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.is_valid_bst(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
