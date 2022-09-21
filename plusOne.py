def plusOne(arr):
    it = len(arr) - 1

    while it >= 0:
        if arr[it] == 9:
            arr[it] = 0
            it -= 1

    if it < 0:
        length = len(arr)
        arr = [1]
        for i in range(length):
            arr.append(0)
    else:
        arr[it] += 1

    return arr
