def reverse_string(s: list) -> list:
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


def sum_digits(n: int) -> int:
    x = 0

    while n > 0:
        x += n % 10
        n //= 10

    return x
