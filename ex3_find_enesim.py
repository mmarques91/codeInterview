import heapq

def find_enesim(arr, n):
    heap = [-el for el in arr]
    heapq.heapify(heap)
    for i in range(n-1):
        heapq.heappop(heap)
    return -heapq.heappop(heap)






