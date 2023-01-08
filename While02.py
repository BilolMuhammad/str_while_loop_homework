def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    leng = len(s)
    sum = 0
    idx = 0
    while leng != 0:
        if s[idx].isalpha():
            sum += 1
        idx += 1
        leng -= 1
    return sum


print(main('s8fg98'))
