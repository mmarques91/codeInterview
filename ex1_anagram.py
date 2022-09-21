def is_anagram(s1, s2):
    #Teste inicial
    if len(s1) != len(s2):
        return False

    #Definição das Harsh tables
    h1 = {}
    h2 = {}

    #Populamento das Harsh Tables
    for ch in s1:
        if ch in h1:
            h1[ch] += 1
        else:
            h1[ch] = 1
    for ch in s2:
        if ch in h2:
            h2[ch] += 1
        else:
            h2[ch] = 1

    #Teste de equivalencia das harshs
    for key in h1:
        if key not in h2 or h1[key] != h2[key]:
            return False

    return True
