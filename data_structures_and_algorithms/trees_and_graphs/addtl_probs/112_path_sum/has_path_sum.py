import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree and an integer targetSum, return true if the tree has a
        root-to-leaf path such that adding up all the values along the path equals targetSum.

        A leaf is a node with no children.

    Constraints:
        The number of nodes in the tree is in the range [0, 5000].
        -1000 <= Node.val <= 1000
        -1000 <= targetSum <= 1000

    """

    def has_path_sum(self, root: TreeNode, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, root.val)]
        curr = 0

        while stack:
            node, curr = stack.pop()

            if not node.left and not node.right and curr == targetSum:
                return True
            else:
                if node.left:
                    stack.append((node.left, curr + node.left.val))

                if node.right:
                    stack.append((node.right, curr + node.right.val))

        return False


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/112_path_sum/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}, targetSum = {item['targetSum']}")
        output = solution.has_path_sum(binary_tree(item["root"]), item["targetSum"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
