def container_vol(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0
    while left < right:
        area = min(arr[left], arr[right]) * (right - left)
        max_area = max(area, max_area)
        if arr[right] > arr[left]:
            left += 1
        else:
            right += 1
    return max_area
