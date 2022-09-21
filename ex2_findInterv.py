#Achar inicio do intervalo
def find_first(arr, n):
    left = 0
    right = len(arr - 1)
    mid = (left + right) // 2
    while left < right :
        if arr[mid] == n and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_last(arr, n):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    while left <= right:
        if arr[mid] == n and arr[mid + 1] > n:
            return mid
        elif arr[mid] > n:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def findinterv(arr, n):
    if n < arr[0] or n > arr[-1] or len(arr) == 0:
        return [-1, -1]
    return [find_first(arr, n), find_last(arr, n)]
