# 插入排序（insertion sort）是一种简单的排序算法，它的工作原理与手动整理一副牌的过程非常相似

def insertion_sort(nums: list[int]):
    """插入排序"""
    # 外循环
    for i in range(1, len(nums)):
        base = nums[i]
        j = i -1 
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = base
    
"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    insertion_sort(nums)
    print("插入排序完成后 nums =", nums)