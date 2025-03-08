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

    def max_depth(self, root: TreeNode):
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

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.max_depth(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
