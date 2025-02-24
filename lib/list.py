class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def sl_list(nums, pos):
    """
    :type nums: list
    :rtype: ListNode
    """
    head = ListNode(None)
    dummy = head
    target = None

    for i, num in enumerate(nums):
        if i == pos:
            target = dummy

        dummy.val = num

        if i == len(nums) - 1:
            dummy.next = target
        else:
            dummy.next = ListNode(None)
            dummy = dummy.next

    return head
