# 开启一个循环，每轮从未排序区间选择最小的元素，将其放到已排序区间的末尾。

def swap(nums: list[int], i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def selection_sort(nums: list[int]):
    l = len(nums)
    min_index = 0  
    # 控制轮数
    for i in range(l):
        # 控制子轮数, 获取到 j 之后最小值 min
        for j in range(i, l):
            if nums[j] < nums[min_index]:
                min_index = j
        # 将最小值与已排序的末尾进行交换
        swap(nums, i, min_index)
    return nums
        
"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    zzl = selection_sort(nums)
    print("选择排序完成后 nums =", zzl)        