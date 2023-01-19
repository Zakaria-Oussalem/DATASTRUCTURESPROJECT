######################################
######################################

# My solution:
def addBinary(a: str, b: str) -> str:
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
def addBinary_b(a: str, b: str) -> str:
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


#####################
####################
def isPalindrome(s: str) -> bool:
    """Function that checks if a string is a palindrome or not
    it only acceptes alphanumeric characters. This solution is an O(n)

    Args:
        s (str): string to check wether it is a palindrole or not

    Returns:
        bool: Whether the string was a palindrome or not
    """
    if len(s.strip()) < 2:
        return True

    accepted = "azertyuiopqsdfghjklmwxcvbn1234567890"
    lifo = []
    s = list(s.lower())
    for i, e in enumerate(s):
        if e in accepted:
            lifo.append(e)
            continue
        else:
            s[i] = ""
    s = "".join(s)

    for i, e in enumerate(s):
        if e == lifo[-1]:
            lifo.pop()
        else:
            return False
    return True


######################
# Remove duplicates #
def removeDuplicates(nums: list[int]):
    for i in range(len(nums)):
        if nums[i] == "_":
            return i
        carry = 0
        for j in range(i + 1, len(nums)):
            j += carry
            print(nums)
            if nums[j] == "_":
                break
            if nums[i] == nums[j]:
                nums.pop(j)
                nums.append("_")
                carry = -1

    return len(nums)
