
class MaxHeap:
    def __init__(self, nums: list[int]):
        
        self.max_heap = nums
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)