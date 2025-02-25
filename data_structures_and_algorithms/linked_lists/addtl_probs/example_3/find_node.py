import json
from lib.test import test_list
from lib.list import sl_list


class Solution(object):
    """
    Description:
        Example 3: Given the head of a linked list and an integer k, return the kth node from the
        end.

        For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return
        the node with value 4, as it is the 2nd node from the end.

    Constraints:
        The linked list has at least one value

    """

    def find_node(self, head, k):
        """
        :type head: ListNode
        :type k: Int
        :rtype: Int
        """
        slow = head
        fast = head
        for i in range(k):
            fast = fast.next
            if fast == None:
                # Not a decent way to check values without this list return
                return None

        while fast:
            slow = slow.next
            fast = fast.next

        return slow


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = (
        "./data_structures_and_algorithms/linked_lists/addtl_probs/example_3/input.json"
    )

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: head = {item['head']}, k = {item['k']}")
        output = solution.find_node(sl_list(item["head"], -1), item["k"])
        test_list(output, item["expected"])


if __name__ == "__main__":
    main()
