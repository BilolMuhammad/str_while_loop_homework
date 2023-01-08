def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    leng = len(s)
    idx = 0
    sum = 0
    while leng != 0:
        if s[idx] == 'a' or s[idx] == 'e' or s[idx] == 'i' or s[idx] == 'o' or s[idx] == 'u':
            sum += 1

        idx += 1
        leng -= 1
    return sum


print(main('bilol'))
