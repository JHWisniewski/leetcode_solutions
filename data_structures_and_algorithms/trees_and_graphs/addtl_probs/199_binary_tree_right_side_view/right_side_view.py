import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree, imagine yourself standing on the right side of it, return
        the values of the nodes you can see ordered from top to bottom.

    Constraints:
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100

    """

    def right_side_view(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        from collections import deque

        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            lvl_length = len(queue)
            ans.append(queue[-1].val)

            for _ in range(lvl_length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/199_binary_tree_right_side_view/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.right_side_view(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
