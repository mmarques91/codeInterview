def resolv_tower(n, source='A', aux='B', dest='C'):
    if n == 1:
        print("From " + source + " To " + dest)
    else:
        resolv_tower(n-1, source, dest, aux)
        print("From " + source + " To " + dest)
        resolv_tower(n-1, aux, source, dest)
