# 全排列问题是回溯算法的一个典型应用。它的定义是在给定一个集合（如一个数组或字符串）的情况下，找出其中元素的所有可能的排列。

'''
Q：输入一个整数数组，其中不包含重复元素，返回所有可能的排列。
'''

def backtrack(state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]):
    # 当状态长度等于元素数量的时候，记录解
    if len(state) == len(choices):
        res.append(list(state))
        return
    # 遍历所有选择
    for i, choice in enumerate(choices):
        # prune
        if not selected[i]:
            # try
            selected[i] = True
            state.append(choice)
            # next
            backtrack(state, choices, selected, res)
            # back
            selected[i] = False
            state.pop()

def permutations_i(nums: list[int]) -> list[list[int]]:
    res = []
    backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
    return res 

reslut = permutations_i(nums = [1, 2, 3])
print(reslut)