# 分治搜索策略

def binary_search(nums: list[int], target: int) -> int:
    """二分查找"""
    n = len(nums)
    # 求解问题 f(0, n-1)
    return dfs(nums, target, 0, n - 1)

def dfs(nums: list[int], target: int, i: int, j: int) -> int:
    """"""
    # 若区间为空，代表无目标元素，则返回 -1
    if i > j: # 终止条件
        return -1
    # 计算中点索引 m
    m = (i + j) // 2
    if nums[m] < target:
        # 递归子问题 f(m + 1, j)
        return dfs(nums, target, m + 1, j)
    elif nums[m] > target:
        return dfs(nums, target, i, m - 1)
    else:
        # 找到目标元素，返回目标索引
        return m
    

"""Driver Code"""
if __name__ == "__main__":
    target = 6
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]

    # 二分查找（双闭区间）
    index = binary_search(nums, target)
    print("目标元素 6 的索引 = ", index)  