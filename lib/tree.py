from collections import deque, Counter


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree(nums: list) -> TreeNode:
    if not nums or nums[0] is None:
        return None

    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1

    while i < len(nums):
        node = queue.popleft()

        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1

        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1

    return root


def bfs_list(root: TreeNode) -> list[list[int]]:
    from collections import deque

    if not root:
        return 0

    queue = deque([root])
    levels = []

    while queue:
        lvl_length = len(queue)
        temp = []

        for _ in range(lvl_length):
            node = queue.popleft()

            if not node:
                temp.append(None)
            else:
                temp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        levels.append(temp)

    return levels


def pop_trailing_nones(vals: list) -> list[int]:
    while not vals[-1]:
        vals.pop()

    return vals


def extract_actual_level_vals(root: TreeNode) -> list[int]:
    levels = bfs_list(root)
    vals = []

    for i, level in enumerate(levels):
        if i == 0 or len(Counter(level)) != 1:
            vals += level

    vals = pop_trailing_nones(vals)

    return vals
