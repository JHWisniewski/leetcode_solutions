import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """ """

    def get_levels(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: list(list[Int])
        """
        from collections import deque

        queue = deque([root])
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

            ans.append(temp)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./miscellaneous/print_levels_of_tree/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}")
        output = solution.get_levels(binary_tree(item["root"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
