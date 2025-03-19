import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree, return the sum of values of its deepest leaves.

    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        1 <= Node.val <= 100

    """

    def deepest_leaves_sum(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        from collections import deque

        if not root:
            return 0

        queue = deque([root])

        while queue:
            lvl_length = len(queue)
            ans = 0

            for _ in range(lvl_length):
                node = queue.popleft()
                ans += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/4_deepest_leaves_sum/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.deepest_leaves_sum(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
