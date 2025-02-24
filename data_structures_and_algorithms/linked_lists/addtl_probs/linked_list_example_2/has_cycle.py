import json
from lib.test import test
from lib.list import ListNode, sl_list


class Solution(object):
    """
    Description:
        Given the head of a linked list with an odd number of nodes head, return the value of the
        node in the middle.

        For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.

    """

    def has_cycle(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: bool
        """
        for i in range(8):
            if not head:
                break
            print(head.val)
            head = head.next

        return 0


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/linked_lists/addtl_probs/linked_list_example_2/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: head = {item['head']}, pos = {item['pos']}")
        output = solution.has_cycle(sl_list(item["head"], item["pos"]))
        test(output, item["expected"])


if __name__ == "__main__":
    main()
