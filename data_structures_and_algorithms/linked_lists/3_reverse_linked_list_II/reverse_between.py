import json
from lib.test import test_list
from lib.list import sl_list, ListNode


class Solution(object):
    """
    Description:
        Given the head of a singly linked list and two integers left and right where left <= right,
        reverse the nodes of the list from position left to position right, and return the reversed
        list.

    Constraints:
        The number of nodes in the list is n.
        1 <= n <= 500
        -500 <= Node.val <= 500
        1 <= left <= right <= n

    """

    def reverse_between(self, head: ListNode, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        curr = head
        prev = None

        # Iterate through to left bound
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1

        # Setup changed list tail and left bound connector
        tail, con = curr, prev

        # Reverse middle of list up to right bound
        while right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            right -= 1

        # Connect left bound to latest previous node
        if con:
            con.next = prev
        else:
            head = prev

        # Connect tail of changed list to right bound
        tail.next = curr

        return head


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/linked_lists/3_reverse_linked_list_II/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: head = {item['head']}")
        output = solution.reverse_between(
            sl_list(item["head"], -1), item["left"], item["right"]
        )
        test_list(output, item["expected"])


if __name__ == "__main__":
    main()
