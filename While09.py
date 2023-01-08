def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    leng = len(s)
    idx = 0
    sum = 0
    while leng != 0:
        sum += int(s[idx])
        idx += 1
        leng -= 1
    return sum


print(main('12456'))
