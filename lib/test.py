from lib.list import ListNode, extract_list


def test(output, expected) -> None:
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


def test_list(l_list: ListNode, expected: list) -> None:
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
