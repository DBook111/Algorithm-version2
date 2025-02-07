# 冒泡排序（bubble sort）通过连续地比较与交换相邻元素实现排序。这个过程就像气泡从底部升到顶部一样，因此得名冒泡排序。

def bubble_sort(nums: list[int]):
    length =  len(nums)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                # swap
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
# 效率优化: 如果某轮“冒泡”中没有执行任何交换操作，
# 说明数组已经完成排序，可直接返回结果。
# 因此，可以增加一个标志位 flag 来监测这种情况，一旦出现就立即返回。
def bubble_sort_with_flag(nums: list[int]):
    length =  len(nums)
    for i in range(length - 1):
        flag = False
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                # swap
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            break

"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2, 6, 9, 8, 4, 0, 6]
    bubble_sort(nums)
    print("冒泡排序完成后 nums =", nums)
    bubble_sort_with_flag(nums)
    print("冒泡排序完成后 nums =", nums) 