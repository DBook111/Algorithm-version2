# init
min_heap, flag = [], 1
max_heap, flag = [], -1

# heapq
import heapq
heapq.heappush(max_heap, flag * 1)
heapq.heappush(max_heap, flag * 3)
heapq.heappush(max_heap, flag * 2)
heapq.heappush(max_heap, flag * 5)
heapq.heappush(max_heap, flag * 4)

# get
peek: int = flag * max_heap[0]

# pop
val = flag * heapq.heappop(max_heap)
val = flag * heapq.heappop(max_heap)
val = flag * heapq.heappop(max_heap)
val = flag * heapq.heappop(max_heap)
val = flag * heapq.heappop(max_heap)

# size
size: int = len(max_heap)

# empty
is_empty: bool = not max_heap

# 输入列表并建堆
min_heap: list[int] = [1, 3, 2, 5, 4]
heapq.heapify(min_heap)

def left(self, i: int) -> int:
    """获取左子节点的索引"""
    return 2 * i + 1

def right(self, i: int) -> int:
    """获取右子节点的索引"""
    return 2 * i + 2

def parent(self, i: int) -> int:
    """获取父节点的索引"""
    return (i - 1) // 2  # 向下整除

def peek(self) -> int:
    """访问堆顶元素"""
    return self.max_heap[0]

def push(self, val: int):
    """元素入堆"""
    # add
    self.max_heap.append(val)
    # heapify
    self.sift_up(self.size() - 1)

def sift_up(self, i: int):
    while True:
        p = self.parent(i)
        if p < 0 or self.max_heap[i] <= self.max_heap[p]:
            break
        self.swap(i, p)
        i = p