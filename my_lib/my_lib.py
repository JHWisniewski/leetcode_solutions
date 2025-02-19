#Test
def foo() -> str:
    """
        :rtype: str
    """
    return "Hello world!"

#Sum digits in an integer number
def sumDigits(n: int) -> int:
    """
        :type n: int
        :rtype: int
    """
    x = 0
    
    while n > 0:
        x += n % 10
        n //= 10

    return x

if __name__ == "__main__":
    print("This is the module file.")