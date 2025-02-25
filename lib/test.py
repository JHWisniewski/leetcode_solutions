def extract_list(head):
    """
    :type head: ListNode
    :rtype: list
    """
    ans = []

    while head:
        ans.append(head.val)
        head = head.next

    return ans


def test(output, expected):
    """
    :type output: Any
    :rtype: Void
    """
    print(f"Output: {output}")
    print(f"Expected Output: {expected}")

    if output == expected:
        print("PASS")
    else:
        print("FAIL")
    print()


def test_list(l_list, expected):
    """
    :type l_list: ListNode
    :type expected: list
    :rtype: Void
    """
    output = extract_list(l_list)
    print(f"Output: {output}")
    print(f"Expected Output: {expected}")

    if output == expected:
        print("PASS")
    else:
        print("FAIL")
    print()
