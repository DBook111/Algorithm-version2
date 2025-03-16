class TreeNode():
    """二叉树节点类"""
    def __init__(self, val: int=0):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

def pre_order(root: TreeNode | None):
    """"""
    if root is None:
        return
    if root.val == 7:
        # record
        res.append(root)
    pre_order(root.left)
    pre_order(root.right)

def pre_order(root: TreeNode):
    """"""
    if root is None:
        return
    # try
    path.append(root)
    if root.val == 7:
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    # back
    path.pop()

# prune
def pre_order(root: TreeNode):
    # prune
    if root is None or root.val == 3:
        return
    # try
    path.append(root)
    if root.val == 7:
        # record
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    # back
    path.pop()

# 框架代码
def backtrack(state: State, choices: list[choice], res: list[state]):
    """"""
    if is_solution(state):
        record()
        return
    for choice