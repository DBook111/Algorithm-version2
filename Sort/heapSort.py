def heap_sort(nums: list[int]):
    """堆排序"""
    # 建堆操作：堆化除叶节点以外的其他所有节点
    for i in range(len(nums) // 2 - 1, -1, -1):
        sift_down(nums, len(nums), i)
    # 从堆中提取最大元素，循环 n-1 轮
    for i in range(len(nums) - 1, 0, -1):
        # 交换根节点与最右叶节点（交换首元素与尾元素）
        nums[0], nums[i] = nums[i], nums[0]
        # 以根节点为起点，从顶至底进行堆化
        sift_down(nums, i, 0)
        
def sift_down(nums: list[int], n: int, i: int):
    """堆的长度为 n , 从节点 i 开始，从顶至底堆化"""
    while True:
        # 判断 i, l, r 中最大值的节点, 记为 ma
        l = 2 * i + 1
        r = 2 * i + 2
        ma = i
        if l < n and nums[l] > nums[ma]:
            ma = l
        if r < n and nums[r] > nums[ma]:
            ma = r
        if ma == i:
            break
        nums[ma], nums[i] = nums[i], nums[ma]
        # 循环向下堆化
        i = ma
    

"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2, 8, 7, 5, 6]
    heap_sort(nums)
    print("堆排序完成后 nums =", nums)