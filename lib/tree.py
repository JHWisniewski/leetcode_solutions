from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree(nums):
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
