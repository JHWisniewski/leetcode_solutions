from lib.list import ListNode, extract_list


def test(output, expected) -> None:
    print(f"Output: {output}")
    print(f"Expected Output: {expected}")

    if output == expected:
        print("PASS")
    else:
        print("FAIL")
    print()


def test_list(l_list: ListNode, expected: list) -> None:
    output = extract_list(l_list)
    print(f"Output: {output}")
    print(f"Expected Output: {expected}")

    if output == expected:
        print("PASS")
    else:
        print("FAIL")
    print()
