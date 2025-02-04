from binarySearchForInsert import *

def binary_search_left_edge(nums: list[int], target: int) -> int:
    """二分查找最左一个 target"""
    # 等价于查找 target 的插入点
    i = binary_search_insertion(nums, target)
    # 未找到 target ，返回 -1
    if i == len(nums) or nums[i] != target:
        return -1
    # 找到 target ， 返回索引 i
    return i

"""Driver Code"""
if __name__ == "__main__":
    # 包含重复元素的数组
    nums = [1, 3, 6, 6, 6, 6, 6, 10, 12, 15]
    # 二分查找左边界和右边界
    target = 6
    index = binary_search_left_edge(nums, target)
    print(f"最左一个元素 {target} 的索引为 {index}")