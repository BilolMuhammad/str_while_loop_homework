def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    leng = len(s)
    idx = 0
    sum = 0
    while leng != 0:
        if s[idx].islower():
            sum += 1
        idx += 1
        leng -= 1
    return sum


print(main('dMFFDkdfg'))
