def two_sum_brute_force(nums: list[int], target: int) -> list[int]:    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            

# 考虑借助一个哈希表，键值对分别为数组元素和元素索引。
def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict:
            return [dict[target - nums[i]], i]
        dict[nums[i]] = i
    return []