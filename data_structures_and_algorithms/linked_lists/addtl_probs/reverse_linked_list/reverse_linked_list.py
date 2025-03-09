import json
from lib.test import test_list
from lib.list import sl_list, ListNode


class Solution(object):
    """
    Description:
        Reverse a given dingly linked list.

    Constraints:
        None

    """

    def reverse_linked_list(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/linked_lists/addtl_probs/reverse_linked_list/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: head = {item['head']}")
        output = solution.reverse_linked_list(sl_list(item["head"], -1))
        test_list(output, item["expected"])


if __name__ == "__main__":
    main()
