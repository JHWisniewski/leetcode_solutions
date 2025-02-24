import json
from lib.test import test
from lib.list import sl_list


class Solution(object):
    """
    Description:
        Given head, the head of a linked list, determine if the linked list has a cycle in it.

        There is a cycle in a linked list if there is some node in the list that can be reached
        again by continuously following the next pointer. Internally, pos is used to denote the
        index of the node that tail's next pointer is connected to. Note that pos is not passed as
        a parameter.

        Return true if there is a cycle in the linked list. Otherwise, return false.

    Constraints:
        The number of the nodes in the list is in the range [0, 10^4].
        -10^5 <= Node.val <= 10^5
        pos is -1 or a valid index in the linked-list.

    """

    def has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = (
        "./data_structures_and_algorithms/linked_lists/addtl_probs/example_2/input.json"
    )

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: head = {item['head']}, pos = {item['pos']}")
        output = solution.has_cycle(sl_list(item["head"], item["pos"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
