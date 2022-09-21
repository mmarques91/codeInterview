def generate(n):
    def paranteses(k, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif k == 0:
            if diff == 0:
                combs.append(''.join(combs))
        else:
            comb.append('(')
            paranteses(k-1, diff+1, comb, combs)
            comb.pop()
            comb.append(')')
            paranteses(k-1, diff-1, comb, combs)
            comb.pop()
    combs = []
    paranteses(2*n, 0, [], combs)
    return combs
