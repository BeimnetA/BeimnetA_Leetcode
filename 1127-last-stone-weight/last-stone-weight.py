class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Obtain two largest stones
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            # Smash the two stones
            result = abs(stone2 - stone1)

            # If result is 0, then continue
            if result == 0:
                continue
            # If result is more than 0, then push result back into heap
            else:
                heapq.heappush(heap, -result)

        # If there is still one stone, then return it. Otherwise return 0.
        return neg(heap[0]) if len(heap) > 0 else 0
