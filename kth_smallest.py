import heapq

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        max_heap = []
        for i in A:
            heapq.heappush(max_heap, -1 * i)
            if (len(max_heap) > B):
                curr_max = heapq.heappop(max_heap)
        return heapq.heappop(max_heap) * -1
