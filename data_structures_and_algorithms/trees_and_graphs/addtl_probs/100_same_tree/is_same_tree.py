import json
from lib.test import test
from lib.tree import TreeNode, binary_tree


class Solution(object):
    """
    Description:
        Given the roots of two binary trees p and q, write a function to check if they are the same
        or not.

        Two binary trees are considered the same if they are structurally identical, and the nodes
        have the same value.

    Constraints:
        The number of nodes in both trees is in the range [0, 100].
        -10^4 <= Node.val <= 10^4

    """

    def is_same_tree(self, p: TreeNode, q: TreeNode):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        stack = [(p, q)]

        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue

            if not p or not q:
                return False

            if p.val != q.val:
                return False
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True

    def is_same_tree_naive(self, p: TreeNode, q: TreeNode):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True

        p_stack, q_stack = [p], [q]

        while p_stack and q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            if p_node and q_node and p_node.val == q_node.val:
                p_stack.append(p_node.left)
                p_stack.append(p_node.right)
                q_stack.append(q_node.left)
                q_stack.append(q_node.right)
            elif not p_node and not q_node:
                continue
            else:
                return False

        return True


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/trees_and_graphs/addtl_probs/100_same_tree/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: p = {item['p']}, q = {item['q']}")
        output = solution.is_same_tree(binary_tree(item["p"]), binary_tree(item["q"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
