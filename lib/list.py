class ListNode(object):
    def __init__(self, x: int):
        self.val = x
        self.next = None


# Build singly-linked list given list of 'nums' and cycle index 'pos'
def sl_list(nums: list, pos: int) -> ListNode:
    head = ListNode(None)
    dummy = head
    target = None

    for i, num in enumerate(nums):
        if i == pos:
            target = dummy

        dummy.next = ListNode(num)

        if i == len(nums) - 1:
            dummy.next.next = target
        else:
            dummy = dummy.next

    return head.next


def extract_list(head: ListNode) -> list[int]:
    ans = []

    while head:
        ans.append(head.val)
        head = head.next

    return ans
