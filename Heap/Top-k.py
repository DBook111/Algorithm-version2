# 给定一个长度为 n 的无序数组 nums ，请返回数组中最大的 k 个元素。

# 方法一：遍历选择
# 方法二：排序

# 方法三：堆
import heapq

def top_k_heap(nums: list[int], k: int) -> list[int]:
    heap = []
    # init
    for i in range(k):
        heapq.heappush(heap, nums[i])
    # loop
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap