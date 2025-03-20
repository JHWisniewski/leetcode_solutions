import json
from lib.test import test
from lib.tree import TreeNode, binary_tree, extract_actual_level_vals


class Solution(object):
    """
    Description:
        You are given the root node of a binary search tree (BST) and a value to insert into the
        tree. Return the root node of the BST after the insertion. It is guaranteed that the new
        value does not exist in the original BST.

        Notice that there may exist multiple valid ways for the insertion, as long as the tree
        remains a BST after insertion. You can return any of them.

    Constraints:
        The number of nodes in the tree will be in the range [0, 10^4].
        -10^8 <= Node.val <= 10^8
        All the values Node.val are unique.
        -10^8 <= val <= 10^8
        It's guaranteed that val does not exist in the original BST.

    """

    def insert_into_bst(self, root: TreeNode, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            root = TreeNode(val)
            return root

        stack = [(root)]

        while stack:
            node = stack.pop()

            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root

                stack.append(node.right)

            elif val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root

                stack.append(node.left)


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/6_insert_into_a_binary_search_tree/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}, val = {item['val']}")
        output = solution.insert_into_bst(binary_tree(item["root"]), item["val"])
        output = extract_actual_level_vals(output)
        test(output, item["expected"])


if __name__ == "__main__":
    main()
