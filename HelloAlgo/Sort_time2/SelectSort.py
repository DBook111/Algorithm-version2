def selection_sort(nums: list[int]):    
    n = len(nums)
    if n == 0:
        return nums
    for i in range(n):
        j = i
        index_min = i
        # 找最小的元素的索引值
        for j in range(i, n):
            if nums[j] < nums[index_min]:
                index_min = j
        nums[i], nums[index_min] = nums[index_min], nums[i]
    return nums

"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    selection_sort(nums)
    print("选择排序完成后 nums =", nums)