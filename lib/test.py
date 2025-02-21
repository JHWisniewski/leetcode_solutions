def test(output, expected):
    """
    :type: Void
    :rtype: Void
    """
    print(f"Output: {output}")
    print(f"Expected Output: {expected}")

    if output == expected:
        print("PASS")
    else:
        print("FAIL")
    print()
