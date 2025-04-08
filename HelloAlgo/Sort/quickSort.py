def partition(nums: list[int], left: int, right: int):
    """哨兵划分"""
    # 以 nums[left] 为基准数
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            # 从右向左找首个小于基准数的元素
            j -= 1
        while i < j and nums[i] <= nums[left]:
            # 从左向右找首个大于基准数的元素
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    # 将基准数交换之两子数组的中间
    nums[i], nums[left] = nums[left], nums[i]
    return i

def quick_sort(nums: list[int], left: int, right: int):
    """快速排序"""
    # 子数组长度为 1 时，终止递归
    if left > right:
        return
    # 哨兵划分
    pivot = partition(nums, left, right)
    # 递归左子数组，右子数组
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)

"""Driver Code"""
if __name__ == "__main__":
    nums = [2, 4, 1, 0, 3, 5]
    # partition(nums, 0, len(nums) - 1)
    # print("哨兵划分完成后 nums =", nums)
    quick_sort(nums, 0, len(nums) - 1)
    print("快速排序完成后 nums =", nums)