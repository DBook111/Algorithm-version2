from collections import deque

class TreeNode:
    def __init__(self, val: int):
        self.val: int = val 
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

def level_order(root: TreeNode | None) -> list[int]:
    """层序遍历"""
    queue: deque[TreeNode] = deque()
    queue.append(root)
    res = []
    while queue:
        node: TreeNode | None = queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res

res = []

def pre_order(root: TreeNode | None):
    if root is None:
        return
    res.append(root.val)
    pre_order(root.left)
    pre_order(root.right)
    
def in_order(root: TreeNode | None):
    """中序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

def post_order(root: TreeNode | None):
    """后序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)    