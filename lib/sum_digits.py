def sum_digits(n):
    """
    :type n: int
    :rtype: int
    """
    x = 0

    while n > 0:
        x += n % 10
        n //= 10

    return x
