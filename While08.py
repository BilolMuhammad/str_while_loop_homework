def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    leng = len(s)
    idx = 0
    sum = 0
    while leng != 0:
        if int(s[idx]) % 2 != 0:
            sum += 1

        idx += 1
        leng -= 1

    return sum


print(main('13547'))
