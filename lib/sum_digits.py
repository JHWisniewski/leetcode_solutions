def sum_digits(n: int) -> int:
    x = 0

    while n > 0:
        x += n % 10
        n //= 10

    return x
