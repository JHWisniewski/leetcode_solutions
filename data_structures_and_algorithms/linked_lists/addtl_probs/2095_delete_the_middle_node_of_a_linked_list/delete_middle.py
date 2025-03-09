import json
from lib.test import test_list
from lib.list import sl_list, ListNode


class Solution(object):
    """
    Description:
        You are given the head of a linked list. Delete the middle node, and return the head of the
        modified linked list.

        The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using
        0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

        For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

    Constraints:
        The number of nodes in the list is in the range [1, 10^5].
        1 <= Node.val <= 10^5

    """

    def delete_middle(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = None

        if head.next:
            fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow.next:
            slow.next = slow.next.next
        else:
            head = None
        return head


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/linked_lists/addtl_probs/2095_delete_the_middle_node_of_a_linked_list/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: head = {item['head']}")
        output = solution.delete_middle(sl_list(item["head"], -1))
        test_list(output, item["expected"])


if __name__ == "__main__":
    main()
