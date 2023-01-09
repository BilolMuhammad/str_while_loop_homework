def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    vowels = 'aeiou'
    sum = 0
    i, c = 0, 0
    while i < len(s):
        if not s[i] in vowels and s[i].isalpha():
            c += 1
        i += 1
    return c


print(main('bilol'))
