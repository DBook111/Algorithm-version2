def bubble_sort(nums: list[int]):
    n = len(nums)
    for i in range(n):
        switch = 0
        for j in range(n-1, i, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                switch = 1
        if switch == 0:
            break
    return nums

"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    bubble_sort(nums)
    print("冒泡排序完成后 nums =", nums)
