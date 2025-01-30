class TreeNode:
    def __init__(self, val: int):
        self.val: int = val 
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def search(self, num: int) -> TreeNode | None:
    """"""
    cur = self._root
    # 
    while cur is not None:
        if cur.val < num:
            cur = cur.right
        elif cur.val > num:
            cur = cur.left
        else:
            break
    
    return cur
