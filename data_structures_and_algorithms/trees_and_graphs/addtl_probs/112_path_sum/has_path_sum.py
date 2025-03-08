import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Write a function that reverses a string. The input string is given as an array of
        characters s.

        You must do this by modifying the input array in-place with O(1) extra memory.

    Constraints:
        1 <= s.length <= 10^5
        s[i] is a printable ascii character.

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

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: root = {item['root']}, targetSum = {item['targetSum']}")
        output = solution.has_path_sum(binary_tree(item["root"]), item["targetSum"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
