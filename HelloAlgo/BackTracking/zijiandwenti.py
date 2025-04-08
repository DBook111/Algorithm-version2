# 给定一个正整数数组 nums 和一个目标正整数 target ，请找出所有可能的组合，使得组合中的元素和等于 target 。
# 给定数组无重复元素，每个元素可以被选取多次。请以列表形式返回这些组合，列表中不应包含重复组合。


def sub_sum_i_naiv(nums: list[int], target: int) -> list[list[int]]:
    state = [] # 子集
    total = 0 # 子集和
    res = [] # 结果列表
    backtrack(state, target, total, nums, res)
    return res

def backtrack(state: list[int], target: int, total: int, choices: list[int], res: list[list[int]]):
    if total == target:
        res.append(list(state))
        return
    # 遍历所有选择
    for i in range(len(choices)):
        if total + choices[i] > target:
            continue
        # 尝试选择当前元素
        state.append(choices[i])
        total += choices[i]
        # 继续搜索
        backtrack(state, target, total, choices, res)
        # 撤销选择
        state.pop()
        total -= choices[i]

"""Driver Code"""
if __name__ == "__main__":
    nums = [3, 4, 5]
    target = 9
    res = sub_sum_i_naiv(nums, target)

    print(f"输入数组 nums = {nums}, target = {target}")
    print(f"所有和等于 {target} 的子集 res = {res}")
    print(f"请注意，该方法输出的结果包含重复集合")