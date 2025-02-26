import json
from lib.test import test_list
from lib.list import sl_list, ListNode


class Solution(object):
    """
    Description:
        Given the head of a sorted linked list, delete all duplicates such that each element
        appears only once. Return the linked list sorted as well.

    Constraints:
        The number of nodes in the list is in the range [0, 300].
        -100 <= Node.val <= 100
        The list is guaranteed to be sorted in ascending order.

    """

    def delete_duplicates(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/linked_lists/2_remove_duplicates_from_sorted_list/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: head = {item['head']}")
        output = solution.delete_duplicates(sl_list(item["head"], -1))
        test_list(output, item["expected"])


if __name__ == "__main__":
    main()
