######################################
######################################

# My solution:
def addBinary(self, a: str, b: str) -> str:
    # Basic case
    if a == "0" or b == "0":
        if a == "0":
            return b
        else:
            return a

    i, j = len(a) - 1, len(b) - 1
    remainder = 0
    result = ""
    while i >= 0 and j >= 0:

        sum_ = int(a[i]) + int(b[j]) + remainder
        result = str(sum_ % 2) + result
        remainder = int(sum_ > 1)
        i -= 1
        j -= 1

    while i >= 0:
        sum_ = int(a[i]) + remainder
        result = str(sum_ % 2) + result
        remainder = int(sum_ > 1)
        i -= 1

    while j >= 0:
        sum_ = int(b[j]) + remainder
        result = str(sum_ % 2) + result
        remainder = int(sum_ > 1)
        j -= 1

    if remainder:
        result = "1" + result

    return result


# Best Solution:
def addBinary(a: str, b: str) -> str:
    """Function that takes two numbers represented with binary strings
    and returns the sum as a binary string.

    Args:
        a (str): banry string 1
        b (str): biinary string 2

    Returns:
        str: result of the sum
    """
    carry = 0
    result = ""

    a = list(a)
    b = list(b)

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        result += str(carry % 2)
        carry //= 2

    return result[::-1]
