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