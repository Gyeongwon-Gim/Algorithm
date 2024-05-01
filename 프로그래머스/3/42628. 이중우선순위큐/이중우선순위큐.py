import heapq 
def solution(operations):
    heap = []
    for order in operations:
        x, y = order.split()
        if x == "I":
            heapq.heappush(heap, int(y))
        else:
            if y == '1':
                if heap:
                    heap.remove(max(heap))
            else:
                if heap:
                    heapq.heappop(heap)
    return [max(heap), heapq.heappop(heap)] if heap else [0, 0]