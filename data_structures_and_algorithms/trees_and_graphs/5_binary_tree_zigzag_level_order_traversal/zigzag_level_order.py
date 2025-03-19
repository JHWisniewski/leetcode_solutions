import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree, return the zigzag level order traversal of its nodes'
        values. (i.e., from left to right, then right to left for the next level and alternate
        between).

    Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -100 <= Node.val <= 100

    """

    def zigzag_level_order(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        from collections import deque

        if not root:
            return []

        queue = deque([root])
        left_to_right = 1
        ans = []

        while queue:
            lvl_length = len(queue)
            temp = []

            for _ in range(lvl_length):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if left_to_right:
                ans.append(temp)
                left_to_right -= 1
            else:
                ans.append(temp[::-1])
                left_to_right += 1

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/5_binary_tree_zigzag_level_order_traversal/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.zigzag_level_order(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
