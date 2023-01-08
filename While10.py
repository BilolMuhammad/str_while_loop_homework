def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    leng = len(s)
    sum = 0
    idx = 0
    while leng != 0:
        if int(s[idx]) % 2 != 0:
            sum += int(s[idx])
        leng -= 1
        idx += 1
    return sum


print(main('123451'))
