import json
from lib.test import test
from lib.list import sl_list


class Solution(object):
    """
    Description:
        Given the head of a singly linked list, return the middle node of the linked list.

        If there are two middle nodes, return the second middle node.

    Constraints:
        The number of nodes in the list is in the range [1, 100].
        1 <= Node.val <= 100

    """

    def middle_node(self, head):
        """
        :type head: ListNode
        :type k: Int
        :rtype: Int
        """
        # Testing output is a list
        ans = []

        slow = head
        fast = None

        # List of size 1
        if head.next:
            fast = head.next.next
        else:
            ans.append(slow.val)
            return ans

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Needed for testing
        while slow and slow.next:
            ans.append(slow.next.val)
            slow = slow.next

        return ans

    def middle_node_leetcodeformat(self, head):
        """
        :type head: ListNode
        :type k: Int
        :rtype: Int
        """
        slow = head
        fast = None

        if head.next:
            fast = head.next.next
        else:
            return slow

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.next


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/linked_lists/1_middle_of_the_linked_list/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: head = {item['head']}")
        output = solution.middle_node(sl_list(item["head"], -1))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
