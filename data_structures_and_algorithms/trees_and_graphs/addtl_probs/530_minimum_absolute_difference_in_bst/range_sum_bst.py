import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a Binary Search Tree (BST), return the minimum absolute difference
        between the values of any two different nodes in the tree.

    Constraints:
        The number of nodes in the tree is in the range [2, 10^4].
        0 <= Node.val <= 10^5

    """

    def get_minimum_difference(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = []
        vals = []
        curr = root
        ans = float("inf")

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                vals.append(curr.val)
                curr = curr.right

        for i in range(1, len(vals)):
            ans = min(ans, vals[i] - vals[i - 1])

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/530_minimum_absolute_difference_in_bst/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.get_minimum_difference(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
