def reverse_string(s: list) -> list:
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    # Two pointers for reversing string
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
        left += 1
        right -= 1

    return s
