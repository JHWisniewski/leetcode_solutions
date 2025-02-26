import json
from lib.test import test_list
from lib.list import sl_list, ListNode


class Solution(object):
    """
    Description:
        Given a linked list, swap every two adjacent nodes and return its head. You must solve the
        problem without modifying the values in the list's nodes (i.e., only nodes themselves may
        be changed.)

    Constraints:
        The number of nodes in the list is in the range [0, 100].
        0 <= Node.val <= 100

    """

    def swap_pairs(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        temp = 0

        while curr and curr.next:
            temp = curr.val
            curr.val = curr.next.val
            curr.next.val = temp
            curr = curr.next.next

        return head


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/linked_lists/addtl_probs/24_swap_nodes_in_pairs/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: head = {item['head']}")
        output = solution.swap_pairs(sl_list(item["head"], -1))
        test_list(output, item["expected"])


if __name__ == "__main__":
    main()
