def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    leng = len(s)
    idx = 0
    sum = 0
    while leng != 0:
        if s[idx].isdigit():
            sum += 1
        leng -= 1
        idx += 1
    return sum


print(main('m23s5'))
