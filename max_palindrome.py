def max_palindrome(stg):
    h1 = {}

    for ch in stg:
        if ch in h1:
            h1[ch] += 1
        else:
            h1[ch] = 1

    length = 0
    have_odd = 0

    for i in range(len(h1)):
        if h1[i] % 2 == 0:
            length += h1[i]
        else:
            have_odd = 1
            length += h1[i] - 1

    return length + have_odd
