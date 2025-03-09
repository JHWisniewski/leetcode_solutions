import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary tree, return an array of the largest value in each row of the
        tree (0-indexed).

    Constraints:
        The number of nodes in the tree will be in the range [0, 10^4].
        -2^31 <= Node.val <= 2^31 - 1

    """

    def largest_values_dfs(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return []

        stack = [(root, 0)]
        ans = []

        while stack:
            node, depth = stack.pop()

            if depth == len(ans):
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return ans

    def largest_values_bfs(self, root: TreeNode):
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
            curr = float("-inf")

            for _ in range(lvl_length):
                node = queue.popleft()
                curr = max(curr, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(curr)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/515_find_largest_value_in_each_tree_row/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.largest_values(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
