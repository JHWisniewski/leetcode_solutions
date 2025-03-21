import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the root of a binary search tree and a target value, return the value in the BST that
        is closest to the target. If there are multiple answers, print the smallest.

    Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        0 <= Node.val <= 10^9
        -10^9 <= target <= 10^9

    """

    def closest_value(self, root: TreeNode, target: float):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :rtype: int
        """
        min_val = root.val
        diff = abs(root.val - target)
        stack = [(root)]

        while stack:
            node = stack.pop()
            curr = abs(node.val - target)

            if curr < diff or (curr == diff and node.val < min_val):
                diff = curr
                min_val = node.val

            # if curr not in diffs:
            #     diffs[curr] = node.val
            # elif diffs[curr] > node.val:
            #     diffs[curr] = node.val

            if node.left and target < node.val:
                stack.append((node.left))
            elif node.right:
                stack.append((node.right))

        return min_val


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/7_closest_binary_search_tree_value/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: root = {item['root']}, target = {item['target']}")
        output = solution.closest_value(binary_tree(item["root"]), item["target"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
